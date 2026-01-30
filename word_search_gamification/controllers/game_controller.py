from odoo import http
from odoo.http import request
import json


class WordSearchGameController(http.Controller):

    @http.route('/word_search/play/<int:game_id>', type='http', auth='user', website=True)
    def play_game(self, game_id, **kwargs):
        """Render the game play interface"""
        game = request.env['word.search.game'].browse(game_id)
        
        if not game.exists():
            return request.not_found()
        
        # Generate the grid
        words = [word.word.upper() for word in game.word_ids]
        
        if not words:
            return request.render('word_search_gamification.no_words_error', {
                'game': game
            })
        
        # Generate grid using the generator
        from ..models.word_search_generator import WordSearchGenerator
        generator = WordSearchGenerator(words, game.grid_size)
        grid = generator.generate()
        
        return request.render('word_search_gamification.game_play_template', {
            'game': game,
            'grid': grid,
            'words': words,
            'grid_size': game.grid_size
        })
    
    @http.route('/word_search/save_attempt', type='json', auth='user')
    def save_attempt(self, game_id, time_spent, score, completed, found_words):
        """Save game attempt"""
        attempt = request.env['word.search.attempt'].create({
            'game_id': game_id,
            'user_id': request.env.user.id,
            'time_spent': time_spent,
            'score': score,
            'completed': completed,
            'found_words_json': json.dumps(found_words)
        })
        
        return {
            'success': True,
            'attempt_id': attempt.id,
            'message': 'Attempt saved successfully!'
        }
    
    @http.route('/word_search/get_leaderboard/<int:game_id>', type='json', auth='user')
    def get_leaderboard(self, game_id):
        """Get leaderboard for specific game"""
        attempts = request.env['word.search.attempt'].search([
            ('game_id', '=', game_id),
            ('completed', '=', True)
        ], order='score desc, time_spent asc', limit=10)
        
        leaderboard = []
        for attempt in attempts:
            leaderboard.append({
                'user': attempt.user_id.name,
                'score': attempt.score,
                'time': attempt.time_spent,
                'date': attempt.played_at.strftime('%Y-%m-%d %H:%M')
            })
        
        return leaderboard

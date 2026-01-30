from odoo import models, fields, api


class WordSearchLeaderboard(models.Model):
    _name = "word.search.leaderboard"
    _description = "Word Search Leaderboard"
    _order = "total_score desc"

    user_id = fields.Many2one("res.users", required=True)

    total_score = fields.Integer(default=0)
    games_played = fields.Integer(default=0)
    best_time = fields.Float(string="Best Time")

    last_played = fields.Datetime()

    @api.model
    def update_leaderboard(self, user_id, score, time_spent):
        """Update or create leaderboard entry for a user"""
        leaderboard = self.search([("user_id", "=", user_id)], limit=1)

        if not leaderboard:
            # Create new leaderboard entry
            leaderboard = self.create({
                "user_id": user_id,
                "total_score": score,
                "games_played": 1,
                "best_time": time_spent,
                "last_played": fields.Datetime.now(),
            })
        else:
            # Update existing leaderboard entry
            vals = {
                "total_score": leaderboard.total_score + score,
                "games_played": leaderboard.games_played + 1,
                "last_played": fields.Datetime.now(),
            }
            
            # Update best time if this one is better
            if not leaderboard.best_time or time_spent < leaderboard.best_time:
                vals["best_time"] = time_spent
            
            leaderboard.write(vals)
        
        return leaderboard

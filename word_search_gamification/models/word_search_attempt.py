from odoo import models, fields, api
from odoo.exceptions import ValidationError


class WordSearchAttempt(models.Model):
    _name = "word.search.attempt"
    _description = "Word Search Attempt"
    _order = "time_spent asc"

    user_id = fields.Many2one(
        "res.users",
        string="Player",
        required=True,
        default=lambda self: self.env.user
    )

    game_id = fields.Many2one(
        "word.search.game",
        string="Game",
        required=True
    )

    time_spent = fields.Float(string="Time Spent (seconds)")
    score = fields.Integer(string="Score")

    completed = fields.Boolean(string="Completed", default=False)

    found_words_json = fields.Text(
        string="Found Words JSON",
        help="Stores found words for analytics"
    )

    played_at = fields.Datetime(default=fields.Datetime.now)

    @api.constrains("time_spent", "score")
    def _check_values(self):
        for record in self:
            if record.time_spent and record.time_spent < 0:
                raise ValidationError("Time spent cannot be negative.")
            if record.score and record.score < 0:
                raise ValidationError("Score cannot be negative.")

    @api.model
    def create(self, vals):
        import logging
        _logger = logging.getLogger(__name__)
        
        attempt = super().create(vals)
        
        _logger.info(f"Attempt created: completed={attempt.completed}, score={attempt.score}, user={attempt.user_id.id}")
        
        # Update leaderboard when new attempt is created (using sudo for permissions)
        if attempt.completed and attempt.score > 0:
            try:
                _logger.info(f"Updating leaderboard for user {attempt.user_id.id}")
                self.env["word.search.leaderboard"].sudo().update_leaderboard(
                    attempt.user_id.id,
                    attempt.score,
                    attempt.time_spent
                )
                _logger.info("Leaderboard updated successfully")
            except Exception as e:
                _logger.error(f"Error updating leaderboard: {str(e)}", exc_info=True)
        else:
            _logger.info(f"Not updating leaderboard: completed={attempt.completed}, score={attempt.score}")
        
        return attempt

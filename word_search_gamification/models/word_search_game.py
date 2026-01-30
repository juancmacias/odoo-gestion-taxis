from odoo import models, fields, api
from odoo.exceptions import ValidationError


class WordSearchGame(models.Model):
    _name = "word.search.game"
    _description = "Word Search Game"
    _order = "create_date desc"

    name = fields.Char(string="Game Name", required=True)
    description = fields.Text(string="Description")

    theme = fields.Char(string="Theme")
    difficulty = fields.Selection([
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard")
    ], default="easy", required=True)

    grid_size = fields.Integer(string="Grid Size", default=10)
    language = fields.Selection([
        ("es", "Spanish"),
        ("en", "English"),
        ("fr", "French")
    ], default="es")

    active_from = fields.Date(string="Active From")
    active_until = fields.Date(string="Active Until")

    word_ids = fields.Many2many(
        "word.search.word",
        "word_search_game_word_rel",
        "game_id",
        "word_id",
        string="Words"
    )

    state = fields.Selection([
        ("draft", "Draft"),
        ("active", "Active"),
        ("archived", "Archived")
    ], default="draft")

    active = fields.Boolean(default=True)

    total_attempts = fields.Integer(
        compute="_compute_total_attempts",
        string="Attempts",
        store=False
    )

    def _compute_total_attempts(self):
        for record in self:
            record.total_attempts = self.env["word.search.attempt"].search_count([
                ("game_id", "=", record.id)
            ]) if record.id else 0

    @api.constrains("grid_size")
    def _check_grid_size(self):
        for record in self:
            if record.grid_size < 5 or record.grid_size > 20:
                raise ValidationError("Grid size must be between 5 and 20.")

    @api.constrains("active_from", "active_until")
    def _check_dates(self):
        for record in self:
            if record.active_from and record.active_until:
                if record.active_from > record.active_until:
                    raise ValidationError("Active from date must be before active until date.")

    def action_activate(self):
        """Activate the game"""
        self.write({'state': 'active'})

    def action_archive(self):
        """Archive the game"""
        self.write({'state': 'archived'})

    def action_set_to_draft(self):
        """Set game back to draft"""
        self.write({'state': 'draft'})

    def action_play_game(self):
        """Open the game play interface"""
        return {
            'type': 'ir.actions.act_url',
            'url': f'/word_search/play/{self.id}',
            'target': 'self',
        }

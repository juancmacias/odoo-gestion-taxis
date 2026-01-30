from odoo import models, fields, api
from odoo.exceptions import ValidationError


class WordSearchWord(models.Model):
    _name = "word.search.word"
    _description = "Word Search Word"
    _rec_name = "word"
    _order = "word asc"

    word = fields.Char(string="Word", required=True)
    category = fields.Char(string="Category")
    language = fields.Selection([
        ("es", "Spanish"),
        ("en", "English"),
        ("fr", "French")
    ], default="es")

    difficulty = fields.Selection([
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard")
    ], default="easy")

    active = fields.Boolean(default=True)

    @api.constrains("word")
    def _check_word(self):
        for record in self:
            if not record.word or len(record.word) < 2:
                raise ValidationError("Word must have at least 2 characters.")
            if len(record.word) > 15:
                raise ValidationError("Word cannot exceed 15 characters.")
            if not record.word.isalpha():
                raise ValidationError("Word must contain only letters.")

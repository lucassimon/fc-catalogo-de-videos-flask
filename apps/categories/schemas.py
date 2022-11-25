from marshmallow import Schema, fields, ValidationError
from kernel_catalogo_videos.core.utils import ACTIVE_STATUS, INACTIVE_STATUS

from apps.messages import Messages

def validate_status(value):
    if value != ACTIVE_STATUS or value != INACTIVE_STATUS:
        raise ValidationError(
            f"The status needs to be {ACTIVE_STATUS} for active or {INACTIVE_STATUS} to inactive ."
        )


class CreateCategorySchema(Schema):
    title = fields.Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    description = fields.Str(required=False)
    status = fields.Integer(validate=validate_status)

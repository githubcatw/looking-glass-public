"""
Looking Glass - backend
Common classes
(c) 2023 githubcatw
"""

from telegram.ext import CallbackContext, ExtBot
from dataclasses import dataclass

from tempfile import TemporaryFile

"""
Custom bot update for sending a photo.
"""
@dataclass
class PhotoUpdate:
    # The user to send the photo to
    user_id: int
    # The photo as an array of bytes
    photo: bytearray

class CustomContext(CallbackContext[ExtBot, dict, dict, dict]):
    """
    Custom CallbackContext class that makes `user_data` available for updates of type
    `WebhookUpdate`.
    """

    @classmethod
    def from_update(
        cls,
        update: object,
        application: "Application",
    ) -> "CustomContext":
        if isinstance(update, PhotoUpdate):
            return cls(application=application, user_id=update.user_id)
        return super().from_update(update, application)

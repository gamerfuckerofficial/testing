# TG-UserBot - A modular Telegram UserBot for Python3.6+. 
# Copyright (C) 2019  Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.


from . import client

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.types.photos import Photos, PhotosSlice


async def get_user_profile_pics(user, limit: int = 0):
    user_photos = await client(GetUserPhotosRequest(
        user_id=user,
        offset=0,
        max_id=0,
        limit=limit
    ))
    photos = user_photos.photos
    if isinstance(user_photos, Photos):
        count = len(photos)
    elif isinstance(user_photos, PhotosSlice):
        count = user_photos.count
    return count, photos
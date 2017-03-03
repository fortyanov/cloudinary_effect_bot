import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config(
  cloud_name="deufevho6",
  api_key="928992861159516",
  api_secret="8CRKvEfL9KoSwJuGILdsbVjiiHs"
)


def upload_photo(url):
    return cloudinary.uploader.upload(url)


def add_filter(public_id, **filters):
    return cloudinary.CloudinaryImage(public_id).build_url(effect="tint:equalize:80:red:50p:blue:60p:yellow:40p")


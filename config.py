# config.py

# Twilio configuration
twilio_account_sid = 'your_account_sid'
twilio_auth_token = 'your_auth_token'
twilio_phone_number = '+your_phone_number'

# Cloudinary configuration
cloudinary.config(
    cloud_name='your_cloud_name',
    api_key='your_api_key',
    api_secret='your_api_secret'
)

# Cooldown configurations
notification_cooldown = 60
api_cooldown = 60
upload_cooldown = 40

import cloudinary

# Twilio configuration
TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'

# Cloudinary configuration
cloudinary.config(
    cloud_name='YOUR_CLOUD_NAME',
    api_key='YOUR_CLOUDINARY_API_KEY',
    api_secret='YOUR_CLOUDINARY_API_SECRET'
)

# Buzzer GPIO pin
BUZZER_PIN = 17

# Location details
LATITUDE = 27.671429184856468
LONGITUDE = 85.33869538051245
GOOGLE_MAPS_LINK = f"https://www.google.com/maps?q={LATITUDE},{LONGITUDE}"

# Cooldowns
NOTIFICATION_COOLDOWN = 60
UPLOAD_COOLDOWN = 40

import os

class Config:
    # Load environment variables if available
    KBB_API_KEY = os.getenv('KBB_API_KEY', 'YOUR_KBB_API_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://username:password@localhost/car_db')

    @staticmethod
    def init_app(app):
        pass

config = Config()

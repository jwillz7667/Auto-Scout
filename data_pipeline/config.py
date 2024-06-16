import os

class Config:
    """
    Configuration class for loading environment variables.
    """

    # Load environment variables if available
    KBB_API_KEY = os.getenv('KBB_API_KEY', 'YOUR_KBB_API_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://username:password@localhost/car_db')

    @staticmethod
    def init_app(app):
        """
        Initialize the application with the given configuration.

        :param app: The application instance to initialize.
        """
        pass

config = Config()

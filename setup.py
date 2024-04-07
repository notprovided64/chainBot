from setuptools import setup

setup(
    name='chainBot',
    version='1.0',
    python_requires='>=3.10.4',
    install_requires=[ 
        'asyncio', 
        'discord', 
        'dotenv', 
        'pyautogui', 
        'mss', 
        'cv2', 
        'PIL', 
        'numpy', 
        'toml', 
    ], 
)

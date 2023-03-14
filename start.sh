echo "Cloning Repo...."
git clone https://github.com/aglink/Shortner-Converter-Bot-V3.git /Shortner-Converter-Bot-V3
cd /Shortner-Converter-Bot-V2
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py

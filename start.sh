if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Helper-Botz/MULTIDB-BOT.git /MULTIDB-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MULTIDB-BOT
fi
cd /MULTIDB-BOT
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py

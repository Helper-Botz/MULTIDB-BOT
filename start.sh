if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Helper-Botz/24BOT.git /24BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /24BOT
fi
cd /24BOT
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 lilsa.py

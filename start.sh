if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/JoeykingTG/JoeyKing.git /JoeyKing
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /JoeyKing
fi
cd /JoeyKing
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py

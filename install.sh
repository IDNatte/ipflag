echo -e "\n----> installing requirements <----\n"

# sudo apt update && sudo apt install python3 python3-tk python3-venv -y

echo -e "\n----> building python executable <----\n"

python3 -m venv env --upgrade-deps && source ./env/bin/activate
pip install -r ./requirements.txt
pyinstaller src/main.py -F -w --hidden-import=requests

echo -e "\n----> Adding plugin to your polybar path <----\n"
echo -e "working on it..."
cp ./dist/main ./ipflag/ipflag
cp -R ./ipflag ~/.config/polybar/

chmod +x ~/.config/polybar/ipflag/label.sh
chmod +x ~/.config/polybar/ipflag/window.sh

echo -e "\n----> Post install <----\n"
echo -e "please follow instruction in README.md @ configuring polybar..."
echo -e "Plugin ready to be used in configuration"
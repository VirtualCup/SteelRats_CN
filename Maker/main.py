from UnrealLocres import UnrealLocres;
from StringHelper import StringHelper;
import csv;
import sys;
import os;

reload(sys) 
sys.setdefaultencoding('utf8')

def get_localization():
	loc_en = UnrealLocres("OriginalFile/Game.locres.en");
	loc_zh = UnrealLocres("OriginalFile/Game.locres.zh");
	loc_en.save_to_csv("en.csv");
	loc_zh.save_to_csv("zh.csv");
	
# get_localization();

def gen_fonts():
	sh = StringHelper();
	sh.code = "dos";
	sh.add_file_text("localization.new.csv");
	sh.add_western();
	sh.add_poland();
	strs = sh.get_chars();

	strs = "\"" + strs + "\""
	tool_path = "\"E:\\Python Localization Helper\\Font\\sfnttool.jar\"";
	font_folder_path = "\"E:\\Python Localization Helper\\Font\\{0}\"";
	font_export_path = "\"SteelRats\\Content\\SteelRats\\UI\\HUD\\Fonts\\{0}\"";

	commandstr = ["java -jar", tool_path, "-s", strs, font_folder_path.format("SourceHanSansSC-Light.ttf"), font_export_path.format("SourceHanSans-Light.ufont")];
	os.system(" ".join(commandstr).encode('mbcs'));
	commandstr = ["java -jar", tool_path, "-s", strs, font_folder_path.format("SourceHanSansSC-Bold.ttf"), font_export_path.format("SourceHanSans-Heavy.ufont")];
	os.system(" ".join(commandstr).encode('mbcs'));
	commandstr = ["java -jar", tool_path, "-s", strs, font_folder_path.format("SourceHanSansSC-Medium.ttf"), font_export_path.format("SourceHanSans-Medium.ufont")];
	os.system(" ".join(commandstr).encode('mbcs'));
	# commandstr = ["java -jar", tool_path, "-s", strs, font_folder_path.format("SourceHanSansSC-Normal.ttf"), font_export_path.format("0138EU27.ufont")];
	# os.system(" ".join(commandstr).encode('mbcs'));


# Text
loc = UnrealLocres("OriginalFile/Game.locres");

loc.load_from_csv("localization.new.csv");
loc.save_to_locres("SteelRats/Content/Localization/Game/zh-Hans/Game.locres");

gen_fonts();

tool_path = "\"E:\\Python Localization Helper\\u4pak.py\""
apk_path = "\"..\\Steel Rats\\SteelRats\\Content\\Paks\\SteelRats-WindowsNoEditor_p.pak\""

commandstr = "python " + tool_path + " pack " + apk_path + " SteelRats\\"
os.system(commandstr.encode('mbcs'));
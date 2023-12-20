#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：setup
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/10/15
#####################################################
from osif import CLS_OSIF

#####################################################
class CLS_Create_TBL_UNIT_TYPE() :
#####################################################

	sOBJ_DB        = ""
	sCHR_TableName = ""

#####################################################
# 初期化
#####################################################
	def __init__( self, in_DB_Obj=None ):
		self.sOBJ_DB        = in_DB_Obj
		self.sCHR_TableName = "TBL_UNIT_TYPE"
		self.__run()
		return



#####################################################
# 実行
#####################################################
	def __run(self):
		#############################
		# テーブルのドロップ
		wQuery = "drop table if exists " + self.sCHR_TableName + ";"
		self.sOBJ_DB.RunQuery( wQuery )
		
		#############################
		# テーブル枠の作成
		wQuery = "create table " + self.sCHR_TableName + "(" + \
					"type     CHAR(7)    NOT NULL," + \
					"class    CHAR(4)    NOT NULL," + \
					"name     CHAR(10)   NOT NULL," + \
					"name_en  CHAR(40)   NOT NULL," + \
					"help     TEXT," + \
					"help_en  TEXT," + \
					" PRIMARY KEY ( type ) ) ;"

#CREATE TABLE Staff
#(id    CHAR(4)    NOT NULL,
#name   TEXT       NOT NULL,
#age    INTEGER    ,
#PRIMARY KEY (id));


		self.sOBJ_DB.RunQuery( wQuery )

#############################
# **** データの挿入 ****
		###駆逐艦
		wHelp    = "小型で小回りがきく戦列艦。主に近距離で火砲や魚雷を使った戦闘に向く。爆雷も搭載でき対潜性能がある。少し輸送ペイロードがあり、輸送任務も可能。機動性能が高い。" + \
				   "防御性能は低い。"
		wHelp_en = "A battleship with a small size and a small turn. Mainly suitable for battles using artillery and torpedoes at close range. It can be equipped with a blast and has anti-submarine performance. There is a little transport payload and transport missions are possible. MV is High. " + \
				   "DF is low."
		self.__insert( "BSDS-DD", "BSDS", "駆逐艦", "Destroyer", wHelp, wHelp_en )
		
		wHelp    = "耐久性能に特化した駆逐艦。前面に装甲シールドが展開でき、艦隊の防御がおこなえる。耐久性能が高い。" + \
				   "機動性能は低い。"
		wHelp_en = "A destroyer specializing in durability. An armored shield can be deployed on the front to protect the fleet. DF is High. " + \
				   "MV is low."
		self.__insert( "BSDS-AM", "BSDS", "装甲駆逐艦", "Armored Destroyer", wHelp, wHelp_en )
		
		wHelp    = "対空戦闘力を向上させた駆逐艦。強力な対空砲と対空レーダを装備し、航空機を迎撃するのに向いている。対空攻撃力が高い。" + \
				   "砲、魚雷に制限がある。耐久性能は低い。"
		wHelp_en = "A destroyer with improved anti-air combat capabilities. Equipped with powerful anti-aircraft guns and anti-aircraft radar, it is suitable for intercepting aircraft. ABA is High. " + \
				   "There are restrictions on artillery and torpedoes. DF is low."
		self.__insert( "BSDS-AD", "BSDS", "防空駆逐艦", "Air Defensive Destroyer", wHelp, wHelp_en )
		
		wHelp    = "ミサイルが搭載可能な駆逐艦。ミサイルによる長射程攻撃が可能になった。電子性能が僅かに向上している。" + \
				   "砲、魚雷、爆雷に制限がある。耐久性能は低い。"
		wHelp_en = "A destroyer that can be equipped with missiles. Long range attacks with missiles are now possible. EL is slightly improved. " + \
				   "There are restrictions on artillery, torpedoes and detonations. DF is low."
		self.__insert( "BSDS-MS", "BSDS", "ミサイル駆逐艦", "Missile Destroyer", wHelp, wHelp_en )
		
		wHelp    = "大量の魚雷を満載し、魚雷戦に特化した駆逐艦。魚雷の一斉発射ができる。機動性能も僅かに向上している。" + \
				   "砲、爆雷に制限がある。耐久性能は低い。主兵装が雷装のため、攻撃が後手になる。"
		wHelp_en = "A destroyer that is full of torpedoes and specialized in torpedo battles. Simultaneous launch of torpedoes. MV is also slightly improved. " + \
				   "There are restrictions on guns and thunderbolts. DF is low. Since the main armament is lightning, the attack will be followed."
		self.__insert( "BSDS-TP", "BSDS", "重雷装艦", "Torpedo Destroyer", wHelp, wHelp_en )
		
		wHelp    = "大型のブースターを装備し、機動力による高速戦闘に特化した駆逐艦。機動性能が高い。" + \
				   "耐久性能は低い。魚雷、爆雷は搭載できなくなり、対潜性能はなくなる。"
		wHelp_en = "A destroyer equipped with a large booster and specialized in high-speed combat with mobility. MV is High. " + \
				   "DF is low. Torpedoes and torpedoes can no longer be installed, and anti-submarine performance is lost."
		self.__insert( "BSDS-AS", "BSDS", "突撃艦", "Assault Destroyer", wHelp, wHelp_en )
		
		wHelp    = "高出力で範囲の広い対潜ソナーと爆雷、対潜攻撃機を搭載し、対潜戦闘に向く駆逐艦。機動性能が高い。" + \
				   "砲、魚雷に制限がある。耐久性能は低い。"
		wHelp_en = "A destroyer that is equipped with anti-submarine sonar, detonation, and anti-submarine attack aircraft with high output and a wide range, suitable for anti-submarine battles. MV is High. " + \
				   "There are restrictions on artillery and torpedoes. DF is low."
		self.__insert( "BSDS-SK", "BSDS", "駆潜艦", "Submarine Killer", wHelp, wHelp_en )
		
		###巡航艦
		wHelp    = "中型で長距離の航行に向いてる艦。中型の火砲による砲戦が得意で、機動性が高く、索敵にも向いている。" + \
				   "艦載機として偵察機が搭載できる。"
		wHelp_en = "A ship that is suitable for medium-sized and long-distance navigation. He is good at medium-sized artillery art, is highly mobile, and is suitable for search. " + \
				   "A reconnaissance aircraft can be mounted as a carrier-based aircraft."
		self.__insert( "BSCR-CC", "BSCR", "巡航艦", "Cruiser", wHelp, wHelp_en )
		
		wHelp    = "対空装備が充実し、迎撃用のミサイルが搭載でき、対航空機、ミサイルに対する防御力が高い。" + \
				   "戦闘機、電子支援機が搭載できる。"
		wHelp_en = "Equipped with anti-aircraft equipment, it can carry missiles for interception, and has high defense against aircraft and missiles. " + \
				   "It can carry fighters and electronic support aircraft."
		self.__insert( "BSCR-AD", "BSCR", "防空巡航艦", "Air Defensive Cruiser", wHelp, wHelp_en )
		
		wHelp    = "多数のミサイルが搭載でき、迎撃用のミサイルも搭載する。ミサイル戦のスペシャリスト。索敵性能が僅かに向上する。" + \
				   "砲撃性能は低い。"
		wHelp_en = "It can carry a large number of missiles, as well as missiles for interception. Missile warfare specialist. Search performance is slightly improved. " + \
				   "Bombardment performance is reduced."
		self.__insert( "BSCR-MS", "BSCR", "ミサイル巡航艦", "Missile Cruiser", wHelp, wHelp_en )
		
		wHelp    = "大型のブースターを搭載し、駆逐艦並みの速度が出せる巡航艦。速い分索敵性能を向上させ、シールドも強化されている。" + \
				   "防御性能が低下し、偵察機が搭載できなくなってる。"
		wHelp_en = "A cruise ship equipped with a large booster and capable of producing a destroyer-like speed. Faster enemy enemy performance is improved and the shield is also strengthened. " + \
				   "The defensive performance has been reduced and the reconnaissance aircraft can not be mounted."
		self.__insert( "BSCR-SP", "BSCR", "高速巡航艦", "Splint Cruiser", wHelp, wHelp_en )
		
		wHelp    = "少数ながら汎用戦闘機が搭載できる巡航艦。航空機による制空、爆撃をおこなうことができる。" + \
				   "機動性能、防御性能は低い。"
		wHelp_en = "A small number of cruise ships that can be equipped with general purpose fighters. It can be used for air control and bombing by aircraft. " + \
				   "Maneuverability and defense performance is reduced."
		self.__insert( "BSCR-AV", "BSCR", "航空巡航艦", "Aviation Cruiser", wHelp, wHelp_en )
		
		wHelp    = "揚陸艇が運用できる巡航艦。機動性能と防御性能が僅かに向上しており、敵の近距離から揚陸艇を送ることができる。" + \
				   "砲撃性能は低い。"
		wHelp_en = "A cruise ship that can operate landing vessels. There is a slight improvement in maneuverability and defense performance, and you can send landing boats from the enemy''s close range. " + \
				   "Bombardment performance is reduced."
		self.__insert( "BSCR-SR", "BSCR", "強襲巡航艦", "Storm Cruiser", wHelp, wHelp_en )
		
		wHelp    = "電子性能が高く、指揮機能をもつ巡航艦。敵の電子妨害を解析し、情報共有する機能をもつ。魚雷、爆雷も搭載できる。" + \
				   "砲撃性能、防御性能は低い。"
		wHelp_en = "A cruise ship with high electronic performance and command function. It has a function to analyze enemy''s electronic interference and share information. It can also be equipped with torpedoes and detonators. " + \
				   "Fire and defense performance is reduced."
		self.__insert( "BSCR-FL", "BSCR", "嚮導艦", "Flotilla Leader Ship", wHelp, wHelp_en )
		
		###戦艦
		wHelp    = "戦列艦の花形。大型の火砲とミサイルを搭載し、装甲やシールドが厚く、対艦戦闘に秀でる。" + \
				   "しかし鈍足で戦闘以外の目的では運用しにくい。"
		wHelp_en = "Flower shape of the battleship. Equipped with large guns and missiles, thick armor and shields, it excels in anti-ship battles. " + \
				   "However, it is slow and difficult to operate for purposes other than combat."
		self.__insert( "BSBB-BB", "BSBB", "戦艦", "Battle Ship", wHelp, wHelp_en )
		
		wHelp    = "防御性能に特化した戦艦。前面に装甲シールドが展開でき、艦隊の防御がおこなえる。" + \
				   "砲撃性能、重い盾を搭載したことで機動性能は低い。また偵察機が搭載できなくなっている。"
		wHelp_en = "A battleship specialized in defensive performance. An armored shield can be deployed on the front, enabling fleet defense. " + \
				   "The bombardment performance and heavy shields reduce maneuverability. Also, the reconnaissance aircraft can not be mounted."
		self.__insert( "BSBB-AM", "BSBB", "装甲戦艦", "Armored Battle Ship", wHelp, wHelp_en )
		
		wHelp    = "駆逐艦、巡航艦、戦艦のいいとこ取りを集約した戦艦。やや機動性があり偵察機と魚雷も搭載できる。" + \
				   "砲撃性能は低い。"
		wHelp_en = "A destroyer, a cruise ship, a battleship that brings together the strengths of a battleship. It is somewhat mobile and can be equipped with a reconnaissance aircraft and a torpedo. " + \
				   "Bombardment performance is reduced."
		self.__insert( "BSBB-BC", "BSBB", "巡航戦艦", "Battle Cruiser", wHelp, wHelp_en )
		
		wHelp    = "大型のブースターを搭載し、巡航艦並みの速度が出せる戦艦。速い分索敵性能を向上させ、シールドも強化されている。" + \
				   "砲撃性能、装甲性能が低下し、偵察機が搭載できなくなっている。"
		wHelp_en = "It is a battleship equipped with a large booster and capable of producing cruise-class speeds. Faster enemy enemy performance is improved and the shield is also strengthened. " + \
				   "Fire and armor performance has been reduced, making it impossible to mount a reconnaissance aircraft."
		self.__insert( "BSBB-SP", "BSBB", "高速戦艦", "Sprint Battle Ship", wHelp, wHelp_en )
		
		wHelp    = "少数ながら汎用戦闘機が搭載できる戦艦。航空機による制空、爆撃をおこなうことができる。" + \
				   "機動性能、防御性能は低い。またミサイルが搭載できなくなっている。"
		wHelp_en = "A few battleships that can be equipped with general-purpose fighters. It can be used for air control and bombing by aircraft. " + \
				   "Maneuverability and defense performance is reduced. Also, missiles can not be loaded."
		self.__insert( "BSBB-AV", "BSBB", "航空戦艦", "Aviation Battle Ship", wHelp, wHelp_en )
		
		wHelp    = "要塞砲が搭載できる規格外の戦艦。艦載用に小型化されたとはいえ、その威力は通常の大型火砲を軽く上回る。" + \
				   "ただし、コストがアホみたいにかかる上、鈍足で艦隊随伴艦としては扱いにくい。"
		wHelp_en = "A nonstandard battleship that can carry a fortress gun. Even though it has been miniaturized for ship-loading, its power is lightly superior to that of a conventional large-sized gun. " + \
				   "However, the cost is like stupid, and it is awkward and difficult to handle as a fleet adjunct."
		self.__insert( "BSBB-ST", "BSBB", "戦略打撃艦", "Strike Battle Ship", wHelp, wHelp_en )
		
		wHelp    = "長距離砲撃戦に特化した戦艦。敵艦隊の射程外から精度の高い砲撃ができる。索敵性能が向上している。" + \
				   "防御性能は低い。またミサイルが搭載できなくなっている。"
		wHelp_en = "A battleship specialized in long range artillery battles. You can fire with high accuracy from outside the range of the enemy fleet. Search performance has been improved. " + \
				   "Defense performance is reduced. Also, missiles can not be loaded."
		self.__insert( "BSBB-HG", "BSBB", "重砲撃艦", "Heavy Gun Ship", wHelp, wHelp_en )
		
		###航空母艦
		wHelp    = "小型の艦載機を大量に運用するための母艦。ほとんどの艦載機が運用できる。運用できる航空戦力数は空母のなかでで一番。" + \
				   "単艦の戦闘力は貧弱。カタパルトが損傷すると艦載機が発進できなくなる。"
		wHelp_en = "A mother ship for operating a large number of small carriers. Most carrier-based aircraft can operate. The number of air force that can be operated is the best among the aircraft carriers. " + \
				   "The battle force of a single ship is poor. If the catapult is damaged, the carrier can not be launched."
		self.__insert( "BSAC-CC", "BSAC", "航空母艦", "Carrier", wHelp, wHelp_en )
		
		wHelp    = "カタパルトの防御力と、艦体の防御力、耐久力をあげた空母。爆撃機以外の艦載機が運用できる。" + \
				   "被弾時の誘爆による二次被害を抑えるため、爆弾を扱う艦載機が運用できないため、航空攻撃力が若干落ちる。"
		wHelp_en = "A carrier with catapult defense, ship hull defense and endurance. Carrier-based aircraft other than bombers can operate. " + \
				   "In order to suppress the secondary damage by the bombing at the time of the shot, the aircraft attacking power falls slightly because the carrier-based aircraft handling the bomb can not be operated."
		self.__insert( "BSAC-AM", "BSAC", "装甲空母", "Armored Carrier", wHelp, wHelp_en )
		
		wHelp    = "艦載機の発進能力をあげて、航空攻撃力をあげた空母。すべての艦載機が運用できる。" + \
				   "カタパルトの精密度が増した分、被弾にはよわくなってる。"
		wHelp_en = "An aircraft carrier that raises the air attack power by raising the launch capability of the carrier. All aircraft carriers can operate. " + \
				   "As the accuracy of the catapults increased, I am more amused by the bullets."
		self.__insert( "BSAC-AT", "BSAC", "攻撃空母", "Attack Carrier", wHelp, wHelp_en )
		
		wHelp    = "戦闘艇の発進デッキを設けた空母。戦闘艇が運用できることで、汎用性があがっている。またすべての艦載機が運用できる。" + \
				   "戦闘艇が搭載できる分、艦載機の搭載機数が少なめになってしまう。"
		wHelp_en = "An aircraft carrier equipped with a launch deck for battle boats. Being able to operate a battle boat raises its versatility. It can also operate all carrier aircraft. " + \
				   "As a battle boat can be loaded, the number of loaded aircraft will be reduced."
		self.__insert( "BSAC-SR", "BSAC", "強襲空母", "Storm Carrier", wHelp, wHelp_en )
		
		wHelp    = "爆撃機専用の空母。大型の爆撃機が多数運用できる。泊地にも降下でき、仮設の飛行場にもなる。無降下でも爆撃機を泊地に降下させられる。" + \
				   "大きな巨体と誘爆しやすい爆弾を満載するため、防御性能は脆弱になってる。"
		wHelp_en = "An aircraft carrier dedicated to bombers. Many large bombers can be operated. It can also be lowered to a place to stay and it will be a temporary airfield. Even if there is no descent, the bomber can be lowered to the bed. " + \
				   "The defense performance is weak because it is full of large giants and bombs that are easy to detonate."
		self.__insert( "BSAC-BO", "BSAC", "爆撃機空母", "Bomber Carrier", wHelp, wHelp_en )
		
		wHelp    = "大型の航空機が運用できる空母。爆撃機空母と違って、電子戦機など支援用の航空機が運用できるのが特徴。" + \
				   "大きな巨体と誘爆しやすい爆弾を搭載するため、防御性能が脆弱になるのは変わらない。"
		wHelp_en = "An aircraft carrier that can operate a large aircraft. Unlike bomber aircraft carriers, it is characterized by the ability to operate support aircraft such as electronic fighters. " + \
				   "Because of the large giants and bombs that are easy to detonate, the defense performance remains vulnerable."
		self.__insert( "BSAC-GI", "BSAC", "巨人機空母", "Giant Aircraft Carrier", wHelp, wHelp_en )
		
		wHelp    = "艦載機も大型機もハイブリッドに運用できる空母。無降下で爆撃機を泊地に降下させられる（回収には自力で軌道上まで来る必要がある）。" + \
				   "全体的な搭載機数は少な目。"
		wHelp_en = "An aircraft carrier that can operate both a carrier-based aircraft and a large aircraft hybrid. You can lower the bomber to a place without descent (you have to come to orbit by yourself for recovery). " + \
				   "The overall number of machines installed is small."
		self.__insert( "BSAC-ST", "BSAC", "戦略空母", "Strike Carrier", wHelp, wHelp_en )
		
		###汎用母艦
		wHelp    = "汎用航空機と機動歩兵で低コストで中距離の防御をするための母艦。" + \
				   "汎用戦闘機の性能の分、本格的な航空戦力を保有する航空母艦との戦力差は否めない。"
		wHelp_en = "A mother ship for low cost, medium distance defense with general purpose aircraft and mobile infantry. " + \
				   "Due to the performance of general-purpose fighters, the difference in strength with aircraft carriers that possess full-scale air force is undeniable."
		self.__insert( "BSGC-GG", "BSGC", "汎用母艦", "General Purpose Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "複数の戦闘艇が運用できる母艦。戦闘艇の搭載数としては戦列艦で最多。その分戦力になる。" + \
				   "単艦の戦闘力は貧弱。"
		wHelp_en = "A mother ship that can operate multiple battle boats. The number of battle boats mounted is the largest in a battleship. It will be the strength of that minute. " + \
				   "The battle force of a single ship is poor."
		self.__insert( "BSGC-BM", "BSGC", "戦闘艇母艦", "Boat Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "歩兵による近接戦闘と、陸戦支援をおこなうための母艦。機動性能、防御性能が高い。" + \
				   "単艦の戦闘力は貧弱。"
		wHelp_en = "A mother ship for close combat by infantry and land support. High maneuverability and defense performance. " + \
				   "The battle force of a single ship is poor."
		self.__insert( "BSGC-IF", "BSGC", "歩兵母艦", "Infantry Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "大型航空機を高速展開させるための母艦。巡航艦並みの速度で移動できる。すべての航空機と陸戦爆撃機が運用できる。" + \
				   "単艦の戦闘力は貧弱。汎用機以外の航空機（大型機）の搭載数は極めて少ない。"
		wHelp_en = "Mother ship for high-speed deployment of large aircraft. Can travel at cruise-class speeds. All aircraft and land battle bombers can operate. " + \
				   "The battle force of a single ship is poor. The number of aircraft (large aircraft) other than general-purpose aircraft is extremely small."
		self.__insert( "BSGC-SP", "BSGC", "高速母艦", "Sprint Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "陸戦攻撃機が運用できる数少ない戦列艦。揚陸艇も運用できる。" + \
				   "単艦の戦闘力は貧弱。陸戦攻撃機を展開するのに泊地へ降下する必要がある。"
		wHelp_en = "One of the few warships that can be operated by land battle aircraft. A landing boat can also be operated. " + \
				   "The battle force of a single ship is poor. It is necessary to descend to a place to deploy land-based attack aircraft."
		self.__insert( "BSGC-LM", "BSGC", "陸戦母艦", "Land Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "防衛兵器を搭載、戦術兵器として運用するためのある意味チートな母艦。" + \
				   "オープンドックのため艦の防御性能は低くなっている。コストと手間がアホみたいにかかるのが致命的難点。"
		wHelp_en = "A cheat mothership with military weapons and operational tactical weapons. " + \
				   "Because of the open dock, the ship''s defense performance is low. It is fatal that cost and effort take like fool."
		self.__insert( "BSGC-DF", "BSGC", "防衛兵器母艦", "Defence Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "機動兵器全般が運用できる超大型母艦。まさに移動要塞。艦載機と重戦闘機、重爆撃機、戦闘艇が搭載できる。搭載数が非常に多い。" + \
				   "船体が大きい分、艦隊戦では的になりやすい。"
		wHelp_en = "A super-large mother ship that can be used by all kinds of mobile weapons. Just a moving fortress. It can carry a carrier-based aircraft, heavy fighters, heavy bombers, and fighter boats. The number of loading is very large. " + \
				   "Because the hull is large, it is easy to be effective in the fleet battle."
		self.__insert( "BSGC-FT", "BSGC", "要塞母艦", "Fortress Mother Ship", wHelp, wHelp_en )
		
		###揚陸艦
		wHelp    = "泊地へ陸戦兵器を輸送する大型の揚陸艦。歩兵、戦車、ヘリが運用できる。野戦砲で支援砲撃もできる。" + \
				   "陸戦攻撃機の運搬もできる。対艦攻撃能力はない。"
		wHelp_en = "A large landing vessel that transports land-based weapons to the destination. Infantry, tanks and helicopters can be operated. You can also support fire with field guns. " + \
				   "Land war attack aircraft can also be transported. There is no anti-ship attack ability."
		self.__insert( "BSLC-LL", "BSLC", "揚陸艦", "Landing Ship", wHelp, wHelp_en )
		
		wHelp    = "機動性能を向上させた揚陸艦。歩兵、戦車、ヘリが運用できる。野戦砲で支援砲撃もできる。" + \
				   "陸戦攻撃機の運搬もできる。対艦攻撃能力はない。"
		wHelp_en = "Landing ship with improved maneuverability. Infantry, tanks and helicopters can be operated. You can also support fire with field guns. " + \
				   "Land war attack aircraft can also be transported. There is no anti-ship attack ability."
		self.__insert( "BSLC-SP", "BSLC", "高速揚陸艦", "Sprint Landing Ship", wHelp, wHelp_en )
		
		wHelp    = "潜航能力のある揚陸艦。歩兵、戦車が運用できる。潜航してるため安全に泊地まで部隊を輸送できる。" + \
				   "対艦攻撃能力はない。また搭載機数は少ない。"
		wHelp_en = "A submarine capable landing vessel. Infantry and tanks can be operated. You can safely transport your troops to the bed because you''re submersible. " + \
				   "There is no anti-ship attack ability. In addition, the number of installed machines is small."
		self.__insert( "BSLC-SM", "BSLC", "潜航揚陸艦", "Landing Submarine Ship", wHelp, wHelp_en )
		
		wHelp    = "艦単体で陸戦揚陸ができる揚陸艦。歩兵、戦闘艇が運用できる。野戦砲も搭載する。" + \
				   "対艦攻撃能力はない。"
		wHelp_en = "Landing ship that can be landed on land battles alone. Infantry and combat boats can operate. Also equipped with field guns. " + \
				   "There is no anti-ship attack ability."
		self.__insert( "BSLC-SR", "BSLC", "強襲揚陸艦", "Storm Landing Ship", wHelp, wHelp_en )
		
		wHelp    = "戦闘車両を輸送する揚陸艦。余計なスペースを排し、戦車だけを多く搭載できるようにした。野戦砲も搭載する。" + \
				   "対艦攻撃能力はない。"
		wHelp_en = "Landing ship that transports combat vehicles. The extra space was eliminated and only tanks could be loaded. Also equipped with field guns. " + \
				   "There is no anti-ship attack ability."
		self.__insert( "BSLC-TK", "BSLC", "戦車揚陸艦", "Tank Landing Ship", wHelp, wHelp_en )
		
		wHelp    = "陸戦指揮機能を備える揚陸艦。陸戦指揮車と連携し、陸戦兵器の指揮を維持できる。歩兵、戦車、揚陸艇が運用できる。野戦砲も搭載する。" + \
				   "対艦攻撃能力はない。"
		wHelp_en = "Landing ship with land command function. Work with land command vehicles and maintain command of land weapons. Infantry, tanks and landing craft can be operated. Also equipped with field guns. " + \
				   "There is no anti-ship attack ability."
		self.__insert( "BSLC-LC", "BSLC", "陸戦指揮艦", "Land War Commander Ship", wHelp, wHelp_en )
		
		wHelp    = "軌道上から輸送機や輸送艇を送る大型揚陸艦。輸送機や輸送艇、揚陸艇が運用できる。地上を攻撃できる戦略レーザを搭載する。" + \
				   "対艦攻撃能力はない。"
		wHelp_en = "A large landing ship that transports transport aircraft and ships from on orbit. Transport aircraft, transport boat, landing boat can be operated. It carries a strategic laser that can attack the ground. " + \
				   "There is no anti-ship attack ability."
		self.__insert( "BSLC-LS", "BSLC", "降下支援艦", "Landing Support Ship", wHelp, wHelp_en )
		
		###潜航艦
		wHelp    = "亜空間潜航が可能な特殊な戦列艦。潜航中はビームやミサイルなどの兵器ではダメージが与えられず、爆雷でしか攻撃できない。" + \
				   "潜水艦も潜航中は魚雷しか使えない。足が遅く、潜航艦以外には随伴できない。"
		wHelp_en = "A special battleship capable of subspace diving. While diving, weapons such as beams and missiles are not damaged and can only be attacked by detonation. " + \
				   "The submarine can only use torpedoes while diving. I am late and I can not accompany other than a submarine."
		self.__insert( "BSSB-SS", "BSSB", "潜航艦", "Submarine", wHelp, wHelp_en )
		
		wHelp    = "潜航装置の出力をあげ、潜航しても高速がだせるようになった潜航艦。これにより高速の機動艦隊にも随伴できるようになった。" + \
				   "装甲性能は低い。小型主砲は搭載できないため、浮上時の戦闘力は低い。"
		wHelp_en = "A submarine that raises the output of the submersible equipment and is capable of providing high speed even when submersible. This has made it possible to accompany the high-speed mobile fleet. " + \
				   "Armor performance is reduced. Because small-sized guns can not be mounted, the combat power at the time of ascent decreases."
		self.__insert( "BSSB-SP", "BSSB", "高速潜航艦", "Sprint Submarine", wHelp, wHelp_en )
		
		wHelp    = "航空機運用が可能な大型潜航艦。少数ながら汎用戦闘機が搭載でき、航空機による制空、爆撃をおこなうことができる。艦載機は潜航したまま発艦（射出）ができる。" + \
				   "ただし艦載機の着艦（収容）時は浮上する必要がある。小型主砲は搭載できないため、浮上時の戦闘力は低い。"
		wHelp_en = "A large submarine capable of aircraft operation. A small number of general-purpose fighters can be mounted, and aircraft can be used for air control and bombing. A carrier-based aircraft can be launched (subjected) while underway. " + \
				   "However, it is necessary to rise when the ship-borne aircraft arrives. Because small-sized guns can not be mounted, the combat power at the time of ascent decreases."
		self.__insert( "BSSB-AV", "BSSB", "潜航空母", "Aviation Submarine", wHelp, wHelp_en )
		
		wHelp    = "揚陸艇が運用できる大型潜航艦。揚陸艇は潜航したまま発艦、着艦ができ、防御性能も高いため、近距離から揚陸艇を強襲揚陸させる奇襲作戦に向いている。" + \
				   "雷撃性能は低い。小型主砲は搭載できないため、浮上時の戦闘力は低い。"
		wHelp_en = "A large submarine capable of operating landing vessels. Because the landing craft can be launched and landing while submersible and has high defense performance, it is suitable for a surprise attack operation in which the landing craft is attacked and landed from a short distance. " + \
				   "Lightning performance is reduced. Because small-sized guns can not be mounted, the combat power at the time of ascent decreases."
		self.__insert( "BSSB-SR", "BSSB", "強襲潜航艦", "Storm Submarine", wHelp, wHelp_en )
		
		wHelp    = "雷撃性能をあげた攻撃型の潜航艦。分散雷撃はできないが、単艦に集中しやすいため敵艦の撃破率があがる。" + \
				   "分散射撃ができない分、複数の艦に対する打撃力は低い。"
		wHelp_en = "An attack-type submarine that gave lightning strike performance. Although distributed lightning strikes can not be made, it is easy to concentrate on a single ship, and the defeat rate of enemy ships increases. " + \
				   "The impact on multiple ships is diminished by the inability to do distributed fire."
		self.__insert( "BSSB-AT", "BSSB", "攻撃潜航艦", "Attack Submarine", wHelp, wHelp_en )
		
		wHelp    = "ミサイルが搭載できる大型潜航艦。陸戦兵器と潜航艇が運用でき、泊地への揚陸が可能。ミサイルは無浮上で発射できる。" + \
				   "機動性能、防御性能は低い。小型主砲は搭載できないため、浮上時の戦闘力は低い。"
		wHelp_en = "A large submarine that can carry missiles. Land warfare weapons and submarines can be operated, and landing to the landing site is possible. Missiles can be launched without flying. " + \
				   "Maneuverability and defense performance is reduced. Because small-sized guns can not be mounted, the combat power at the time of ascent decreases."
		self.__insert( "BSSB-ST", "BSSB", "戦略潜航艦", "Strike Submarine", wHelp, wHelp_en )
		
		wHelp    = "電子戦が可能な潜航艦。潜航時の速度、電子性能をあげ、潜航したまま機雷の敷設ができる。" + \
				   "雷撃性能、防御性能は低い。小型主砲は搭載できないため、浮上時の戦闘力は低い。"
		wHelp_en = "A submarine capable of electronic warfare. The speed at the time of dive and the electronic performance can be increased, and laying of mines can be done while diving. " + \
				   "Lightning performance, defense performance is reduced. Because small-sized guns can not be mounted, the combat power at the time of ascent decreases."
		self.__insert( "BSSB-RS", "BSSB", "遊撃艦", "Raid Ship", wHelp, wHelp_en )
		
		###防護艦
		wHelp    = "電子戦、近接防御能力が高い、防御専用の護衛艦。艦隊に随伴して事前索敵、電子戦に対する防御をおこなう。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "Electronic warfare, a defensive defense ship with high proximity defense ability. Adhere to the fleet and defend against advance search and electronic warfare. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESCV-EE", "ESCV", "防護艦", "Escort Corvet", wHelp, wHelp_en )
		
		wHelp    = "対潜性能を向上させた防護艦。爆雷を搭載し、潜航艦の索敵性能が向上している。" + \
				   "潜航艦以外への対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "Protective ship with improved anti-submarine performance. Equipped with detonation, the submarine''s search capability has been improved. " + \
				   "There is no anti-ship attack power other than submarines. I can not act on a single ship."
		self.__insert( "ESCV-MP", "ESCV", "対潜防護艦", "Maritime Patrol Corvet", wHelp, wHelp_en )
		
		wHelp    = "早期警戒型の防護艦。電子性能が向上し、警戒レーダによって他艦の対空戦闘をサポートする。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "An early warning type protective ship. Electronic performance is improved and alert radar supports anti-aircraft combat of other ships. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESCV-WA", "ESCV", "警戒防護艦", "Warning Corvet", wHelp, wHelp_en )
		
		wHelp    = "専用の接近専用武器を搭載し、格闘戦による近接防御ができる防護艦。機動性能、防御性能、探知性能にも優れる。" + \
				   "攻撃範囲は非常に短い。単艦では行動できない。"
		wHelp_en = "A protective ship equipped with a special approach weapon and capable of melee defense by fighting. It has excellent maneuverability, defense performance, and detection performance. " + \
				   "The attack range is very short. I can not act on a single ship."
		self.__insert( "ESCV-SG", "ESCV", "格闘戦艦", "Struggl Battle Ship", wHelp, wHelp_en )
		
		###護衛艦
		wHelp    = "対空防御能力が高い護衛艦。対空戦能力が高く、迎撃用のミサイルが搭載でき、航空機とミサイルから艦隊を防御する。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "An escort ship with high anti-air defense capabilities. It has high anti-aircraft capability, can be equipped with missiles for interception, and protects the fleet from aircraft and missiles. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESFG-EE", "ESFG", "護衛艦", "Escort Frigate", wHelp, wHelp_en )
		
		wHelp    = "防御性能に特化した護衛艦。前面に大型の装甲シールドが展開でき、艦隊の防御がおこなえる。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "An escort ship specialized in defensive performance. A large armored shield can be deployed on the front, enabling fleet defense. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESFG-AM", "ESFG", "装甲護衛艦", "Armored Escort Frigate", wHelp, wHelp_en )
		
		wHelp    = "汎用戦闘機が搭載できる護衛艦。航空機による制空戦闘をおこなうことができる。" + \
				   "対艦攻撃力はない（搭載機も爆装できなくなる）。単艦では行動できない。"
		wHelp_en = "An escort ship that can carry a general-purpose fighter. It is possible to perform air combat by aircraft. " + \
				   "There is no anti-ship attack ability (the mounted aircraft can not be detonated). I can not act on a single ship."
		self.__insert( "ESFG-AV", "ESFG", "航空護衛艦", "Aviation Escort Frigate", wHelp, wHelp_en )
		
		wHelp    = "陸戦歩兵が搭載でき、護衛対象の艦に移譲してきた歩兵を迎撃する護衛艦。" + \
				   "対艦攻撃力はない。単艦では行動できない。陸戦隊は基地でしか入れ替えできない。"
		wHelp_en = "Landguard infantry can carry, and escort ship intercepts infantry handed over to target ship of escort. " + \
				   "There is no anti-ship attack power. I can not act on a single ship. Land squadrons can only be replaced at the base."
		self.__insert( "ESFG-LE", "ESFG", "陸戦護衛艦", "Land War Escort Frigate", wHelp, wHelp_en )
		
		###護衛母艦
		wHelp    = "制空用の艦載機で防空を担う空母型の護衛艦。戦闘機、偵察機、電子作戦機が搭載できる。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "An aircraft carrier-type escort ship that carries out air defense on a carrier-based aircraft for air defense. It can carry fighter planes, reconnaissance planes, and electronic warplanes. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESEC-EE", "ESEC", "護衛母艦", "Escort Carrier", wHelp, wHelp_en )
		
		wHelp    = "戦闘艇が搭載できる母艦。戦闘艇が運用でき、戦闘艇により近距離を防御する。実質対艦攻撃ができる。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "A mother ship that can carry battle boats. A battle boat can operate and defend a short distance by a battle boat. It is possible to attack a real anti-ship. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESEC-BM", "ESEC", "護衛艇母艦", "Escort Boat Mother Ship", wHelp, wHelp_en )
		
		wHelp    = "制空用の艦載機をサポートし、迎撃力を向上させた母艦。要撃機、戦闘機、空戦型の機動歩兵が搭載できる。" + \
				   "対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "A mother ship that supports aircraft carriers for air defense and has improved interception power. It can be equipped with interceptors, fighters, and air combat type mobile infantry. " + \
				   "There is no anti-ship attack power. I can not act on a single ship."
		self.__insert( "ESEC-IC", "ESEC", "要撃空母", "Intercept Carrier", wHelp, wHelp_en )
		
		wHelp    = "対潜用の艦載機を専用に扱う母艦。対潜攻撃機、対潜哨戒機を搭載し、艦載機による対潜性能が高い。" + \
				   "潜航艦以外への対艦攻撃力はない。単艦では行動できない。"
		wHelp_en = "A mother ship that deals exclusively with anti-submarine carriers. Equipped with anti-submarine attack aircraft, anti-submarine patrol aircraft, anti-submarine performance by ship-borne aircraft is high. " + \
				   "There is no anti-ship attack power other than submarines. I can not act on a single ship."
		self.__insert( "ESEC-MP", "ESEC", "対潜空母", "Maritime Patrol Carrier", wHelp, wHelp_en )
		
		###偵察艦
		wHelp    = "索敵性能が高い、偵察専用の艦。大きさは巡航艦くらい。機動性能、ステルス性能、電子性能が高い。" + \
				   "防御性能は低く、武装はない。"
		wHelp_en = "A ship dedicated to reconnaissance with high search enemy performance. The size is about a cruise ship. High maneuverability, stealth performance and electronic performance. " + \
				   "Low defensive performance, no armed."
		self.__insert( "SSRE-RR", "SSRE", "偵察艦", "Recommend Ship", wHelp, wHelp_en )
		
		wHelp    = "潜航能力のある偵察艦。潜航したまま偵察行動ができる。" + \
				   "武装はない。"
		wHelp_en = "A submarine capable reconnaissance ship. You can do reconnaissance activities while submersible. " + \
				   "There is no armed."
		self.__insert( "SSRE-SM", "SSRE", "偵察潜行艦", "Recommend Submarine", wHelp, wHelp_en )
		
		wHelp    = "電子戦の影響を全く受けないで偵察ができる特殊偵察艦。鈍足。単艦で要所に配置し、警戒任務がおこなえる。" + \
				   "機動性能、防御性能は低い。"
		wHelp_en = "A special reconnaissance ship capable of reconnaissance without any impact from electronic warfare. I am at a loss. A single ship can be placed at a key location and capable of guarding missions. " + \
				   "Maneuverability and defense performance is reduced."
		self.__insert( "SSRE-DP", "SSRE", "通報艦", "Dispatch Ship", wHelp, wHelp_en )
		
		###輸送艦
		wHelp    = "大量の資源や兵器が運べる輸送専用の艦。艦船以外はなんでも運べる。" + \
				   "鈍足のため機動部隊の随伴には向かない。"
		wHelp_en = "A ship dedicated to transport that can carry large amounts of resources and weapons. You can carry anything except ships. " + \
				   "It is not suitable for the companion of the task force because it is slow."
		self.__insert( "SSTR-TT", "SSTR", "輸送艦", "Transport Ship", wHelp, wHelp_en )
		
		wHelp    = "高速性能をあげた輸送艦。機動部隊に随伴できる。" + \
				   "ペイロードは輸送艦より小さい。"
		wHelp_en = "Transport ship that raised high speed performance. It can accompany the task force. " + \
				   "The payload is smaller than the transport ship."
		self.__insert( "SSTR-SP", "SSTR", "高速輸送艦", "Splint Transport Ship", wHelp, wHelp_en )
		
		wHelp    = "潜航能力のある輸送艦。潜航できるため、安全に貨物が運べる。" + \
				   "ペイロードは輸送艦より小さい。"
		wHelp_en = "A transport ship with submersible capabilities. The cargo can be transported safely because it can be submerged. " + \
				   "The payload is smaller than the transport ship."
		self.__insert( "SSTR-SM", "SSTR", "潜航輸送艦", "Transport Submarine", wHelp, wHelp_en )
		
		###補給艦
		wHelp    = "補給物資を搭載し、戦場で他船の補給をおこなう艦。" + \
				   "鈍足のため機動部隊の随伴には向かない。"
		wHelp_en = "A ship that carries supplies and supplies other ships on the battlefield. " + \
				   "It is not suitable for the companion of the task force because it is slow."
		self.__insert( "SSSS-SS", "SSSS", "補給艦", "Supply Ship", wHelp, wHelp_en )
		
		wHelp    = "高速性能をあげた補給艦。機動部隊に随伴できる。" + \
				   "補給量は補給艦より少ない。"
		wHelp_en = "A supply ship with high speed performance. It can accompany the task force. " + \
				   "The supply amount is less than the supply ship."
		self.__insert( "SSSS-SP", "SSSS", "高速補給艦", "Splint Supply Ship", wHelp, wHelp_en )
		
		wHelp    = "潜航能力のある補給艦。潜航できるため補給物資が安全に運べる。" + \
				   "補給量は補給艦より少ない。補給時は浮上する必要がある。"
		wHelp_en = "A submarine capable supply ship. Supplies can be transported safely as they can dive. " + \
				   "The supply amount is less than the supply ship. At the time of replenishment, it is necessary to rise."
		self.__insert( "SSSS-SM", "SSSS", "潜航補給艦", "Supply Submarine", wHelp, wHelp_en )
		
		###多用途支援艦
		wHelp    = "あらゆる戦略機能を有し、多用途に使える支援艦。陸戦兵器、戦闘艇が搭載できる。" + \
				   "武器はなく、防御性能、機動性能は低い。"
		wHelp_en = "A versatile support ship with all strategic functions. Land war weapons, battle boats can be mounted. " + \
				   "There is no weapon, and defense performance and maneuverability are low."
		self.__insert( "SSMS-MM", "SSMS", "多用途支援艦", "Multipurpose Support Ship", wHelp, wHelp_en )
		
		wHelp    = "撃沈した船や大型の荷物を輸送（牽引）するための支援艦。装甲が戦艦並みに厚い。" + \
				   "武器はなく、機動性能は低い。"
		wHelp_en = "Support ship to transport (tow) sinking ships and large packages. Armor is thick like a battleship. " + \
				   "There is no weapon and maneuverability is low."
		self.__insert( "SSMS-SL", "SSMS", "曳航艦", "Salvage Ship", wHelp, wHelp_en )
		
		wHelp    = "浮遊兵器の設置と回収をおこなうための支援艦。掃海艇も搭載できる。" + \
				   "武器はなく、機動性能は低い。"
		wHelp_en = "A support ship to install and collect floating weapons. Minesweeper can also be installed. " + \
				   "There is no weapon and maneuverability is low."
		self.__insert( "SSMS-LY", "SSMS", "敷設回収艦", "Laying Ship", wHelp, wHelp_en )
		
		wHelp    = "土木作業や艦の修理をするための支援艦。牽引ビームで宇宙ゴミを操作できる。防御性能は高い。" + \
				   "武器はなく、機動性能は低い。"
		wHelp_en = "Support ship for civil engineering and ship repair. Space trash can be operated with a tow beam. Defense performance is high. " + \
				   "There is no weapon and maneuverability is low."
		self.__insert( "SSMS-WK", "SSMS", "工作艦", "Work Ship", wHelp, wHelp_en )
		
		wHelp    = "戦場で資源を採掘するための支援艦。息を吸うように採掘できる。" + \
				   "武器はなく、防御性能、機動性能は低い。"
		wHelp_en = "A support ship for mining resources on the battlefield. You can mine to breathe. " + \
				   "There are no weapons, and defense and maneuverability are low."
		self.__insert( "SSMS-MN", "SSMS", "資源採掘艦", "Mining Ship", wHelp, wHelp_en )
		
		wHelp    = "巨大な転送装置を搭載した支援艦。味方の船を転送したり、敵に爆弾を送りつけたりできる。" + \
				   "武器はなく、防御性能、機動性能は低い。"
		wHelp_en = "A support ship equipped with a huge transfer device. You can transfer friendly ships and send bombs to enemies. " + \
				   "There are no weapons, and defense and maneuverability are low."
		self.__insert( "SSMS-TR", "SSMS", "転送艦", "Transfer Ship", wHelp, wHelp_en )
		
		wHelp    = "戦場の地形を把握したり、気象予測をするための支援艦。" + \
				   "武器はなく、防御性能、機動性能は低い。"
		wHelp_en = "A support ship for understanding the topography of the battlefield and forecasting weather." + \
				   "There are no weapons, and defense and maneuverability are low."
		self.__insert( "SSMS-WO", "SSMS", "気象観測艦", "Weather Observation Ship", wHelp, wHelp_en )
		
		###戦闘支援艦
		wHelp    = "大型砲と強力なシールドと迎撃ミサイルを搭載し、長距離砲撃支援とミサイル防御を担える支援艦。機動性能にも優れる。" + \
				   "防御性能は低い。"
		wHelp_en = "A support ship equipped with a large artillery, powerful shields, and interceptor missiles to support long-range artillery support and missile defense. Excellent maneuverability. " + \
				   "Defense performance is low."
		self.__insert( "SSBS-SS", "SSBS", "戦闘支援艦", "Battle Support Ship", wHelp, wHelp_en )
		
		wHelp    = "電子性能と戦術指揮機能に優れる支援艦。戦場の前衛で戦闘指揮ができる。" + \
				   "防御性能は低い。"
		wHelp_en = "A support ship with excellent electronic performance and tactical command functions. You can command battles on the battlefield front guard. " + \
				   "Defense performance is low."
		self.__insert( "SSBS-TC", "SSBS", "戦術指揮艦", "Tactical Command Ship", wHelp, wHelp_en )
		
		wHelp    = "空戦隊の指揮機能に優れる支援艦。航空機の作戦行動範囲を延ばせる。対空戦闘力もある。" + \
				   "防御性能は低い。"
		wHelp_en = "A support ship with excellent command functions of Air Squadron. Extend the range of aircraft operations. There is also anti-air combat power. " + \
				   "Defense performance is low."
		self.__insert( "SSBS-AI", "SSBS", "航空支援艦", "Airstrike Support Ship", wHelp, wHelp_en )
		
		wHelp    = "護衛艦をたくさん付けることができる支援艦。被弾した護衛艦を回収したり、艦に護衛艦を付けて後送したりできる。" + \
				   "防御性能は低い。"
		wHelp_en = "A support ship with many escort ships. You can collect the escort ships that were hit, or you can attach them to the ship and send them back. " + \
				   "Defense performance is low."
		self.__insert( "SSBS-ES", "SSBS", "護衛支援艦", "Escort Support Ship", wHelp, wHelp_en )
		
		wHelp    = "潜航能力がある支援艦。潜航したまま潜航艦の補給ができる。" + \
				   "防御性能は低い。また、小型主砲、対空砲がないため、浮上時の戦闘力は低い。"
		wHelp_en = "Support ship with submarine capability. Submarine can be replenished while submerged. " + \
				   "Defense performance is low. Also, since there are no small main guns and anti-aircraft guns, the combat power at the time of ascent is reduced."
		self.__insert( "SSBS-SM", "SSBS", "潜航支援艦", "Submarine Support Ship", wHelp, wHelp_en )
		
		wHelp    = "高い電子戦能力をもつ支援艦。マップ全体に強力なジャミングがかけられる。電子戦に対する抵抗力も高い。" + \
				   "防御性能は低い。"
		wHelp_en = "Support ship with high electronic warfare capability. Powerful jamming is applied to the entire map. High resistance to electronic warfare. " + \
				   "Defense performance is low."
		self.__insert( "SSBS-EL", "SSBS", "電子支援艦", "Electronic Support Ship", wHelp, wHelp_en )
		
		wHelp    = "無人標的機を搭載し、練習訓練により艦隊や戦隊の練度をあげる訓練用の支援艦。練習用設備として戦艦、空母の装備も搭載できる。" + \
				   "防御性能は低い。"
		wHelp_en = "A support ship for training that is equipped with unmanned target aircraft and improves the fleet and squadron by training. As a training facility, it can also be equipped with battleships and aircraft carriers. " + \
				   "Defense performance is low."
		self.__insert( "SSBS-TN", "SSBS", "練習支援艦", "Training Support Ship", wHelp, wHelp_en )
		




		###航空機


		wHelp    = "巡航艦や戦艦に搭載できるよう機構を施した小型偵察機。武器はない。" + \
				   "機体が小さいため、他の汎用戦闘機と違って巡航艦以上であればたいてい搭載可能なのがメリット。"
		wHelp_en = "A small reconnaissance aircraft equipped with a mechanism that can be mounted on a cruise ship or battleship. There is no weapon. " + \
				   "Unlike other general-purpose fighters, the advantage of being smaller than a general-purpose fighter is that it can usually be installed on cruise ships or more."
		self.__insert( "MUMA-RA", "MUMA", "汎用偵察機", "General Purpose Recommender", wHelp, wHelp_en )
		



		###機動歩兵
		wHelp    = "人型の戦闘歩兵。機動歩兵としての性能は平凡だが、空戦も陸戦もできる。"
		wHelp_en = "Humanoid fighting infantry. Performance as a mobile infantry is mediocre, but it can be air combat or land battle."
		self.__insert( "MUMS-GP", "MUMS", "汎用型", "General Purpose Type", wHelp, wHelp_en )
		



		###戦闘艇
		wHelp    = "対艦戦闘用の小型戦闘艇。装甲が厚く、大型砲、ロケット、魚雷も搭載できる。" + \
				   "航空機、機動歩兵によわい。"
		wHelp_en = "Small battle boat for anti-ship battle. It has thick armor and can also carry large guns, rockets and torpedoes. " + \
				   "We are vulnerable to aircraft, mobile infantry."
		self.__insert( "MUMB-BB", "MUMB", "戦闘艇", "Battle Boat", wHelp, wHelp_en )
		








		
#############################
		
		#############################
		# データの確認
		wQuery = "select * from " + self.sCHR_TableName + ";"
		self.sOBJ_DB.RunQuery( wQuery )
		
		wRes = self.sOBJ_DB.GetQueryStat()
		wNum = len(wRes['Responce']['Data'])
		wTable = ""
		for wLine in wRes['Responce']['Data'] :
			wTable = wTable + str(wLine) + '\n'
		CLS_OSIF.sPrn( wTable )
		return


#####################################################
	def __insert( self, in_Type, in_Class, in_Name, in_NameEN, in_Help, in_HelpEN ):
		wQuery = "insert into " + self.sCHR_TableName + " values (" + \
					"'" + in_Type +   "'," + \
					"'" + in_Class +  "'," + \
					"'" + in_Name +   "'," + \
					"'" + in_NameEN + "'," + \
					"'" + in_Help +   "'," + \
					"'" + in_HelpEN + "'" + \
					") ;"
		
		self.sOBJ_DB.RunQuery( wQuery )
		return



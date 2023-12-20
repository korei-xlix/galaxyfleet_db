#! /bin/sh
#####################################################
# ::ProjectName= Star Region - Run File  
# ::github= https://github.com/lucida3rd/starregion  
# ::Admin= Lucida（lucida3hai@twitter.com）  
# ::Twitter URL= https://twitter.com/lucida3hai  
#
# ::Update= 2020/9/10
# ::Version= 0.0.0.0
#####################################################

#function testa () {
#	aav="a"
#}
#testa
#echo $aav
#exit

#####################################################
# プロセスID取得
function Get_PID () {
	wCHR_PS_PID="null"
	wCHR_PS_Name=$1
	wCHR_PS_File=$2
	
	#############################
	# ID名から実行中プロセスを抽出 ファイルに書く
	ps -e | grep -w $wCHR_PS_Name > $wCHR_PS_File
	
	#############################
	# ファイルの存在チェック
	if [[ ! -e $wCHR_PS_File ]]; then
		return
	fi
	
	#############################
	# 中身のチェック
	wCHR_PS_Line=`find . -name $wCHR_PS_File | wc -l`
	if [[ $wCHR_PS_Line != 1 ]]; then
		return
	fi
	
	#############################
	# PIDの取り出し
	### ファイルから1行抜き出し
	while read wPS_Line
	do
		wPS_Line=`echo $wPS_Line`
		break
	done < $wCHR_PS_File
	
	#############################
	# ファイル削除
	rm -f $wCHR_PS_File
	
	### 空白で区切り 配列化
	wPS_ARR=(${wPS_Line//,/ })
	### やっとこPID
	wCHR_PS_PID=`echo ${wPS_ARR[0]}`
	
	return
}

#####################################################
# プロセスKILL
function Kill_P () {
	#############################
	# PIDの取り出し
###	wCHR_PS_PID=`Get_PID $1 $2`
	Get_PID $1 $2
	
	if [[ $wCHR_PS_PID == "null" ]]; then
		echo "Kill_P::プロセスの検索に失敗しました"
		return
	fi
	
	#############################
	# プロセスKILL
	kill $wCHR_PS_PID &
	
	#############################
	# プロセス表示
	ps
}



#####################################################
# 開始
function Command_Start () {
	#############################
	# 開始メッセージ
	echo "############################"
	echo "  Start up, Star Region !!"
	echo "############################"
	
	#############################
	# CygServer起動 (PostgreSQL用)
	/usr/sbin/cygserver.exe &
	
	#############################
	# PostgreSQL起動
	pg_ctl start
	pg_ctl status
	echo "Postgre SQL Started !"
	
	#############################
	# uwsgi server起動
##	uwsgi --master --https 127.0.0.1:9090,/etc/pki/Server/server.crt,/etc/pki/Server/server.key --wsgi-file strg_uwsgi/run.py
	
	### ※Ctrl+C を押すまでアイドル
	
	#############################
	# PostgreSQL停止
	pg_ctl stop
	pg_ctl status
	echo "Postgre SQL Stopped !"

	#############################
	# CygServer停止
	Kill_P cygserver strg_cs.txt
	
	echo "############################"
	echo "  Stopped, Star Region"
	echo "############################"
}



#####################################################
# 更新
###wCHR_Updated="off"
wCHR_InstFile="strg_uwsgi/data/inst.txt"
wCHR_InstTag="[Installed-STRG]"

function Check_Update () {
	wCHR_Updated="off"
	wCHR_GoUpdate=$1
	#############################
	# ファイルの存在チェック
	if [[ ! -e $wCHR_InstFile ]]; then
		echo "Instファイルがありません:" $wCHR_InstFile
		exit
	fi
	
##	#############################
##	# 中身のチェック
##	wUpdateLine=`find . -name $wCHR_InstFile | wc -l`
##	if [[ $wUpdateLine == 0 ]]; then
##		return
##	fi
	
	#############################
	# 済タグの検索
	while read wUpdateLine
	do
		### ファイルから1行抜き出して 半角スペースで配列化
		wUpdateLine_1=`echo $wUpdateLine`
		wUpdate_ARR=(${wUpdateLine_1//,/ })
		
		for wUpdate_Moji in ${wUpdate_ARR[@]}
		do
			if [ \( "$wUpdate_Moji" == "$wCHR_InstTag" \) ]; then
				wCHR_Updated="on"
				break
			fi
		done
		if [[ $wCHR_Updated == "on" ]]; then
###			echo "[!!!Detected!!]"
			break
		fi
	done < $wCHR_InstFile
	
	#############################
	# 更新コマンド以外かつ 済でない場合 =アプデを実施する
	if [ \( $wCHR_GoUpdate == 1 \) -a \( $wCHR_Updated == "off" \) ]; then
		Command_Update 0
	fi
}

function Command_Update () {
	wCHR_GoCheck=$1
	#############################
	# 更新コマンドからの場合 チェックをおこなう
	if [ \( $wCHR_GoCheck == 1 \) ]; then
		Check_Update 0
	fi
	
	#############################
	# 済の場合 確認をおこなう
	if [ \( $wCHR_Updated == "on" \) ]; then
		echo "既にアップデートが実施されています"
		read -p "実行しますか？[Yes=y No=others] " wInput
		if [ \( $wInput != "y" \) ]; then
			return
		fi
	fi
	
	#############################
	# 開始メッセージ
	echo "############################"
	echo "  Update Start"
	echo "############################"
	
	#############################
	# 更新実行



	#############################
	# 済記録
	wCHR_DATE=`date +%Y`"-"`date +%m`"-"`date +%d`
	wCHR_TIME=`date +%H`":"`date +%M`":"`date +%S`
	
	wCHR_Inst=$wCHR_InstTag" "$0" "$wCHR_DATE" "$wCHR_TIME
	echo $wCHR_Inst >> $wCHR_InstFile
	
}



#####################################################
# テスト
function Command_Test () {
	echo "#########################"
	echo "  Start, Test mode !!"
	echo "#########################"
	
	uwsgi --master --https 127.0.0.1:9090,/etc/pki/Server/server.crt,/etc/pki/Server/server.key --wsgi-file strg_uwsgi/test.py
	
	echo "#########################"
	echo "  Stopped test"
	echo "#########################"
	
}



#####################################################
# 書式
function View_Command () {
	echo "書式: bash strg_run.sh [option]"
	echo "option:"
	echo "  start  .. Star Region 開始"
###	echo "  stop   .. Star Region 停止"
	echo "  update .. アップデート実行"
	echo "  test   .. uwsgiテストモード ※アクセスチェック時のみ使用"
}



#####################################################
# メイン処理

#############################
# 引数チェック
if [ $# -ne 1 ]; then
	View_Command
	exit
fi
opt_comm=$1
opt_comm=${opt_comm,,}

###if [ \( "$opt_comm" != "start" \) -a \( "$opt_comm" != "stop" \) -a \( "$opt_comm" != "update" \) -a \( "$opt_comm" != "test" \) ] ; then
if [ \( "$opt_comm" != "start" \) -a \( "$opt_comm" != "update" \) -a \( "$opt_comm" != "test" \) ] ; then
	echo "範囲外のオプション"
	View_Command
	exit
fi

###wCHR_Updated="off"
###wCHR_InstFile="strg_uwsgi/data/inst.txt"

#############################
# コマンド= update - 更新
if [ \( "$opt_comm" == "update" \) ] ; then
	Command_Update 1
	exit
fi

#############################
# 更新チェック
Check_Update 1

exit


#############################
# コマンド= start - 開始
if [ \( "$opt_comm" == "start" \) ] ; then
	Command_Start

#############################
# コマンド= update - 更新
###elif [ \( "$opt_comm" == "update" \) ] ; then
###	Command_Update
###
#############################
# コマンド= test - テストモード
elif [ \( "$opt_comm" == "test" \) ] ; then
	Command_Test
###else

fi

exit



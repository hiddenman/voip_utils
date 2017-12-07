#!/usr/bin/python
import sys
import string
import datetime
import calendar
import MySQLdb
import time

host = 'localhost'
user = 'root'
passwd = ''
db = 'ambs'

regexps = [',$','[[:space:]]+']

log_fname = './clean_codes.log'
log_fd = None

def log(msg=''):
    log_fd.write('%s %s\n' % (str(datetime.datetime.now()), msg))
    


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

# cursor.execute("SELECT ID,DEST_CODES FROM DEST WHERE DEST_CODES REGEXP('%s')" % regexp)
#cursor.execute('SELECT ID,DEST_CODES FROM DEST')    
#rows = cursor.fetchall()
#log('Got %d rows' % (len(rows)))
#print 'Got %d rows' % (len(rows))
#for row in rows:
#    codes_id = row[0]
#    codes = row[1]
#    codes_clean = clean_codes(codes)
#    if (codes != codes_clean):
#        log('Replace codes [id:%s str:%s] with [%s]' % (codes_id,codes,codes_clean))
#        cursor.execute("UPDATE DEST SET DEST_CODES='%s' WHERE ID=%d" % (codes_clean,int(codes_id)))
for month in range(1,13):
    for day in range(calendar.monthrange(2008,month)[1]):
        #print day
        #cursor.execute("DELETE FROM CDR WHERE BILL_DATE=%s" % (str('2008-'+str(month)+'-'+str(day))))
        print "DELETE FROM CDR WHERE BILL_DATE=%s" % (str('2008-'+str(month)+'-'+str(day))))
        time.sleep(1)
        
log('Done')
cursor.close()

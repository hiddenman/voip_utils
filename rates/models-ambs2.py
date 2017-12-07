# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Accounting(models.Model):
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    start_time = models.TextField(db_column='START_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    nasport = models.CharField(max_length=90, db_column='NASPORT', blank=True) # Field name made lowercase.
    nasip = models.CharField(max_length=45, db_column='NASIP', blank=True) # Field name made lowercase.
    nasid = models.CharField(max_length=90, db_column='NASID', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=150, db_column='USERNAME', blank=True) # Field name made lowercase.
    octets_in = models.IntegerField(null=True, db_column='OCTETS_IN', blank=True) # Field name made lowercase.
    octets_out = models.IntegerField(null=True, db_column='OCTETS_OUT', blank=True) # Field name made lowercase.
    framedip = models.CharField(max_length=45, db_column='FRAMEDIP', blank=True) # Field name made lowercase.
    session_time = models.IntegerField(null=True, db_column='SESSION_TIME', blank=True) # Field name made lowercase.
    rate = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='RATE', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    term_id = models.IntegerField(null=True, db_column='TERM_ID', blank=True) # Field name made lowercase.
    result = models.IntegerField(null=True, db_column='RESULT', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    ani = models.CharField(max_length=75, db_column='ANI', blank=True) # Field name made lowercase.
    dnis = models.CharField(max_length=75, db_column='DNIS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACCOUNTING'

class AcloseStat(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    aclose_id = models.IntegerField(null=True, db_column='ACLOSE_ID', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(unique=True, null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    dest_id = models.IntegerField(unique=True, null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    code = models.CharField(unique=True, max_length=90, db_column='CODE', blank=True) # Field name made lowercase.
    stat_acd = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='STAT_ACD', blank=True) # Field name made lowercase.
    stat_asr = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='STAT_ASR', blank=True) # Field name made lowercase.
    stat_shcalls = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='STAT_SHCALLS', blank=True) # Field name made lowercase.
    stat_compl = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='STAT_COMPL', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    all_mins = models.IntegerField(null=True, db_column='ALL_MINS', blank=True) # Field name made lowercase.
    close_num = models.IntegerField(null=True, db_column='CLOSE_NUM', blank=True) # Field name made lowercase.
    rparam_id = models.IntegerField(null=True, db_column='RPARAM_ID', blank=True) # Field name made lowercase.
    close_state = models.IntegerField(null=True, db_column='CLOSE_STATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACLOSE_STAT'

class Actions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    actname = models.CharField(max_length=600, db_column='ACTNAME', blank=True) # Field name made lowercase.
    form_id = models.IntegerField(null=True, db_column='FORM_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ACTIONS'

class Agents(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='NAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AGENTS'

class Alerts(models.Model):
    dest_id = models.IntegerField(unique=True, db_column='DEST_ID') # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='PRICE', blank=True) # Field name made lowercase.
    asr = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='ASR', blank=True) # Field name made lowercase.
    acd = models.IntegerField(null=True, db_column='ACD', blank=True) # Field name made lowercase.
    ccount = models.IntegerField(null=True, db_column='CCOUNT', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=765, db_column='EMAIL', blank=True) # Field name made lowercase.
    alert_hour = models.IntegerField(null=True, db_column='ALERT_HOUR', blank=True) # Field name made lowercase.
    alert = models.IntegerField(null=True, db_column='ALERT', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(unique=True, null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    from_tm = models.IntegerField(null=True, blank=True)
    to_tm = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ALERTS'

class AniExp(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    ani_exp = models.CharField(unique=True, max_length=90, db_column='ANI_EXP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ANI_EXP'

class AniGroup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(unique=True, null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    grpname = models.CharField(unique=True, max_length=300, db_column='GRPNAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ANI_GROUP'

class AniSet(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    grp_id = models.IntegerField(unique=True, null=True, db_column='GRP_ID', blank=True) # Field name made lowercase.
    setname = models.CharField(unique=True, max_length=300, db_column='SETNAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ANI_SET'

class AniTypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    type = models.IntegerField(null=True, db_column='TYPE', blank=True) # Field name made lowercase.
    ani = models.CharField(unique=True, max_length=60, db_column='ANI', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ANI_TYPES'

class AniTypeNames(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    tname = models.CharField(unique=True, max_length=60, db_column='TNAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ANI_TYPE_NAMES'

class AsList(models.Model):
    net_id = models.IntegerField(null=True, db_column='NET_ID', blank=True) # Field name made lowercase.
    asn = models.IntegerField(unique=True, null=True, db_column='ASN', blank=True) # Field name made lowercase.
    as_alias = models.CharField(max_length=90, db_column='AS_ALIAS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AS_LIST'

class AutocloseRules(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    site_id = models.IntegerField(unique=True, null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    dest_id = models.IntegerField(unique=True, null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    code = models.CharField(unique=True, max_length=90, db_column='CODE', blank=True) # Field name made lowercase.
    period_range = models.IntegerField(null=True, db_column='PERIOD_RANGE', blank=True) # Field name made lowercase.
    min_calls_cnt = models.IntegerField(null=True, db_column='MIN_CALLS_CNT', blank=True) # Field name made lowercase.
    uniq_calls = models.IntegerField(null=True, db_column='UNIQ_CALLS', blank=True) # Field name made lowercase.
    min_asr = models.IntegerField(null=True, db_column='MIN_ASR', blank=True) # Field name made lowercase.
    min_acd = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='MIN_ACD', blank=True) # Field name made lowercase.
    max_short = models.IntegerField(null=True, db_column='MAX_SHORT', blank=True) # Field name made lowercase.
    min_compl = models.IntegerField(null=True, db_column='MIN_COMPL', blank=True) # Field name made lowercase.
    and_or = models.IntegerField(null=True, db_column='AND_OR', blank=True) # Field name made lowercase.
    not_close = models.IntegerField(null=True, db_column='NOT_CLOSE', blank=True) # Field name made lowercase.
    close_cnt = models.IntegerField(null=True, db_column='CLOSE_CNT', blank=True) # Field name made lowercase.
    close_hours = models.IntegerField(null=True, db_column='CLOSE_HOURS', blank=True) # Field name made lowercase.
    hours_step = models.IntegerField(null=True, db_column='HOURS_STEP', blank=True) # Field name made lowercase.
    mgr_flag = models.IntegerField(null=True, db_column='MGR_FLAG', blank=True) # Field name made lowercase.
    op_flag = models.IntegerField(null=True, db_column='OP_FLAG', blank=True) # Field name made lowercase.
    sup_flag = models.IntegerField(null=True, db_column='SUP_FLAG', blank=True) # Field name made lowercase.
    add_email = models.CharField(max_length=765, db_column='ADD_EMAIL', blank=True) # Field name made lowercase.
    sys_user = models.CharField(max_length=150, db_column='SYS_USER', blank=True) # Field name made lowercase.
    no_breakouts = models.IntegerField(null=True, db_column='NO_BREAKOUTS', blank=True) # Field name made lowercase.
    mail_only = models.IntegerField(null=True, db_column='MAIL_ONLY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AUTOCLOSE_RULES'

class AutoTt(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code = models.CharField(unique=True, max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    cause = models.IntegerField(null=True, db_column='CAUSE', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(unique=True, null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(unique=True, null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    calls_count = models.IntegerField(null=True, db_column='CALLS_COUNT', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='STATUS', blank=True) # Field name made lowercase.
    tt_date = models.DateField(unique=True, null=True, db_column='TT_DATE', blank=True) # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True) # Field name made lowercase.
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AUTO_TT'

class BalanceHistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    balance_date = models.DateField(null=True, db_column='BALANCE_DATE', blank=True) # Field name made lowercase.
    balance = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='BALANCE', blank=True) # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    currency = models.CharField(max_length=9, db_column='CURRENCY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'BALANCE_HISTORY'

class Buhdocs(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    act = models.TextField(db_column='ACT', blank=True) # Field name made lowercase.
    acc = models.TextField(db_column='ACC', blank=True) # Field name made lowercase.
    acc_fact = models.TextField(db_column='ACC_FACT', blank=True) # Field name made lowercase.
    act_num = models.IntegerField(unique=True, db_column='ACT_NUM') # Field name made lowercase.
    acc_num = models.IntegerField(unique=True, db_column='ACC_NUM') # Field name made lowercase.
    acc_fact_num = models.IntegerField(unique=True, db_column='ACC_FACT_NUM') # Field name made lowercase.
    doc_date = models.DateField(unique=True, null=True, db_column='DOC_DATE', blank=True) # Field name made lowercase.
    doc_year = models.IntegerField(null=True, db_column='DOC_YEAR', blank=True) # Field name made lowercase.
    doc_month = models.IntegerField(null=True, db_column='DOC_MONTH', blank=True) # Field name made lowercase.
    doc_period = models.IntegerField(null=True, db_column='DOC_PERIOD', blank=True) # Field name made lowercase.
    op_mail_state = models.IntegerField(null=True, db_column='OP_MAIL_STATE', blank=True) # Field name made lowercase.
    buh_mail_state = models.IntegerField(null=True, db_column='BUH_MAIL_STATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'BUHDOCS'

class BuhClientAttr(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    client_name = models.CharField(max_length=384, blank=True)
    client_inn = models.CharField(max_length=45, blank=True)
    client_kpp = models.IntegerField(null=True, blank=True)
    client_address = models.CharField(max_length=765, blank=True)
    client_service = models.CharField(max_length=765, blank=True)
    client_unit = models.CharField(max_length=96, blank=True)
    client_count = models.FloatField(null=True, blank=True)
    client_tax_proc = models.CharField(max_length=96, blank=True)
    email = models.CharField(max_length=384, blank=True)
    gen_period = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'BUH_CLIENT_ATTR'

class CardsCharge(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    uid = models.IntegerField(unique=True, null=True, db_column='UID', blank=True) # Field name made lowercase.
    charge_sum = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='CHARGE_SUM', blank=True) # Field name made lowercase.
    charge_flag = models.IntegerField(null=True, db_column='CHARGE_FLAG', blank=True) # Field name made lowercase.
    charge_date = models.DateField(null=True, db_column='CHARGE_DATE', blank=True) # Field name made lowercase.
    done_date = models.DateTimeField(db_column='DONE_DATE') # Field name made lowercase.
    class Meta:
        db_table = u'CARDS_CHARGE'

class CardsPay(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    term_id = models.IntegerField(null=True, db_column='TERM_ID', blank=True) # Field name made lowercase.
    summ = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SUMM', blank=True) # Field name made lowercase.
    paydate = models.DateField(null=True, db_column='PAYDATE', blank=True) # Field name made lowercase.
    dbdate = models.DateField(null=True, db_column='DBDATE', blank=True) # Field name made lowercase.
    oper = models.CharField(max_length=150, db_column='OPER', blank=True) # Field name made lowercase.
    pay_type = models.IntegerField(null=True, db_column='PAY_TYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CARDS_PAY'

class Cdr(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    class Meta:
        db_table = u'CDR'

class Cdrbuffer(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    orig_rate_id = models.IntegerField(null=True, db_column='ORIG_RATE_ID', blank=True) # Field name made lowercase.
    term_rate_id = models.IntegerField(null=True, db_column='TERM_RATE_ID', blank=True) # Field name made lowercase.
    sale_oper_id = models.IntegerField(null=True, db_column='SALE_OPER_ID', blank=True) # Field name made lowercase.
    sale_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SALE_COST', blank=True) # Field name made lowercase.
    buy_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='BUY_COST', blank=True) # Field name made lowercase.
    sale_rate_id = models.IntegerField(null=True, db_column='SALE_RATE_ID', blank=True) # Field name made lowercase.
    buy_rate_id = models.IntegerField(null=True, db_column='BUY_RATE_ID', blank=True) # Field name made lowercase.
    forward_client = models.IntegerField(null=True, db_column='FORWARD_CLIENT', blank=True) # Field name made lowercase.
    forward_rate = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='FORWARD_RATE', blank=True) # Field name made lowercase.
    forward_cost = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='FORWARD_COST', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDRBUFFER'

class CdrbufferRead(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    orig_rate_id = models.IntegerField(null=True, db_column='ORIG_RATE_ID', blank=True) # Field name made lowercase.
    term_rate_id = models.IntegerField(null=True, db_column='TERM_RATE_ID', blank=True) # Field name made lowercase.
    sale_oper_id = models.IntegerField(null=True, db_column='SALE_OPER_ID', blank=True) # Field name made lowercase.
    sale_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SALE_COST', blank=True) # Field name made lowercase.
    buy_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='BUY_COST', blank=True) # Field name made lowercase.
    sale_rate_id = models.IntegerField(null=True, db_column='SALE_RATE_ID', blank=True) # Field name made lowercase.
    buy_rate_id = models.IntegerField(null=True, db_column='BUY_RATE_ID', blank=True) # Field name made lowercase.
    forward_client = models.IntegerField(null=True, db_column='FORWARD_CLIENT', blank=True) # Field name made lowercase.
    forward_rate = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='FORWARD_RATE', blank=True) # Field name made lowercase.
    forward_cost = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='FORWARD_COST', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDRBUFFER_READ'

class CdrBill000000(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    tbltype = models.IntegerField(primary_key=True, db_column='TBLTYPE') # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_SYS_PRICE', blank=True) # Field name made lowercase.
    dst_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_SYS_PRICE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    src_oper = models.IntegerField(null=True, db_column='SRC_OPER', blank=True) # Field name made lowercase.
    dst_oper = models.IntegerField(null=True, db_column='DST_OPER', blank=True) # Field name made lowercase.
    src_dest = models.IntegerField(null=True, db_column='SRC_DEST', blank=True) # Field name made lowercase.
    dst_dest = models.IntegerField(null=True, db_column='DST_DEST', blank=True) # Field name made lowercase.
    src_rid = models.IntegerField(null=True, db_column='SRC_RID', blank=True) # Field name made lowercase.
    dst_rid = models.IntegerField(null=True, db_column='DST_RID', blank=True) # Field name made lowercase.
    src_code = models.CharField(max_length=60, db_column='SRC_CODE', blank=True) # Field name made lowercase.
    dst_code = models.CharField(max_length=60, db_column='DST_CODE', blank=True) # Field name made lowercase.
    max_code = models.CharField(max_length=60, db_column='MAX_CODE', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_BILL_TIME', blank=True) # Field name made lowercase.
    dst_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_BILL_TIME', blank=True) # Field name made lowercase.
    src_bill_date = models.DateField(null=True, db_column='SRC_BILL_DATE', blank=True) # Field name made lowercase.
    dst_bill_date = models.DateField(null=True, db_column='DST_BILL_DATE', blank=True) # Field name made lowercase.
    server_id = models.IntegerField(null=True, db_column='SERVER_ID', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    succ_flag = models.IntegerField(null=True, db_column='SUCC_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDR_BILL000000'

class CdrBill201004(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    tbltype = models.IntegerField(primary_key=True, db_column='TBLTYPE') # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_SYS_PRICE', blank=True) # Field name made lowercase.
    dst_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_SYS_PRICE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    src_oper = models.IntegerField(null=True, db_column='SRC_OPER', blank=True) # Field name made lowercase.
    dst_oper = models.IntegerField(null=True, db_column='DST_OPER', blank=True) # Field name made lowercase.
    src_dest = models.IntegerField(null=True, db_column='SRC_DEST', blank=True) # Field name made lowercase.
    dst_dest = models.IntegerField(null=True, db_column='DST_DEST', blank=True) # Field name made lowercase.
    src_rid = models.IntegerField(null=True, db_column='SRC_RID', blank=True) # Field name made lowercase.
    dst_rid = models.IntegerField(null=True, db_column='DST_RID', blank=True) # Field name made lowercase.
    src_code = models.CharField(max_length=60, db_column='SRC_CODE', blank=True) # Field name made lowercase.
    dst_code = models.CharField(max_length=60, db_column='DST_CODE', blank=True) # Field name made lowercase.
    max_code = models.CharField(max_length=60, db_column='MAX_CODE', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_BILL_TIME', blank=True) # Field name made lowercase.
    dst_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_BILL_TIME', blank=True) # Field name made lowercase.
    src_bill_date = models.DateField(null=True, db_column='SRC_BILL_DATE', blank=True) # Field name made lowercase.
    dst_bill_date = models.DateField(null=True, db_column='DST_BILL_DATE', blank=True) # Field name made lowercase.
    server_id = models.IntegerField(null=True, db_column='SERVER_ID', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    succ_flag = models.IntegerField(null=True, db_column='SUCC_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDR_BILL201004'

class CdrBill201005(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    tbltype = models.IntegerField(primary_key=True, db_column='TBLTYPE') # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_SYS_PRICE', blank=True) # Field name made lowercase.
    dst_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_SYS_PRICE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    src_oper = models.IntegerField(null=True, db_column='SRC_OPER', blank=True) # Field name made lowercase.
    dst_oper = models.IntegerField(null=True, db_column='DST_OPER', blank=True) # Field name made lowercase.
    src_dest = models.IntegerField(null=True, db_column='SRC_DEST', blank=True) # Field name made lowercase.
    dst_dest = models.IntegerField(null=True, db_column='DST_DEST', blank=True) # Field name made lowercase.
    src_rid = models.IntegerField(null=True, db_column='SRC_RID', blank=True) # Field name made lowercase.
    dst_rid = models.IntegerField(null=True, db_column='DST_RID', blank=True) # Field name made lowercase.
    src_code = models.CharField(max_length=60, db_column='SRC_CODE', blank=True) # Field name made lowercase.
    dst_code = models.CharField(max_length=60, db_column='DST_CODE', blank=True) # Field name made lowercase.
    max_code = models.CharField(max_length=60, db_column='MAX_CODE', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_BILL_TIME', blank=True) # Field name made lowercase.
    dst_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_BILL_TIME', blank=True) # Field name made lowercase.
    src_bill_date = models.DateField(null=True, db_column='SRC_BILL_DATE', blank=True) # Field name made lowercase.
    dst_bill_date = models.DateField(null=True, db_column='DST_BILL_DATE', blank=True) # Field name made lowercase.
    server_id = models.IntegerField(null=True, db_column='SERVER_ID', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    succ_flag = models.IntegerField(null=True, db_column='SUCC_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDR_BILL201005'

class CdrBill201006(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    tbltype = models.IntegerField(primary_key=True, db_column='TBLTYPE') # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_SYS_PRICE', blank=True) # Field name made lowercase.
    dst_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_SYS_PRICE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    src_oper = models.IntegerField(null=True, db_column='SRC_OPER', blank=True) # Field name made lowercase.
    dst_oper = models.IntegerField(null=True, db_column='DST_OPER', blank=True) # Field name made lowercase.
    src_dest = models.IntegerField(null=True, db_column='SRC_DEST', blank=True) # Field name made lowercase.
    dst_dest = models.IntegerField(null=True, db_column='DST_DEST', blank=True) # Field name made lowercase.
    src_rid = models.IntegerField(null=True, db_column='SRC_RID', blank=True) # Field name made lowercase.
    dst_rid = models.IntegerField(null=True, db_column='DST_RID', blank=True) # Field name made lowercase.
    src_code = models.CharField(max_length=60, db_column='SRC_CODE', blank=True) # Field name made lowercase.
    dst_code = models.CharField(max_length=60, db_column='DST_CODE', blank=True) # Field name made lowercase.
    max_code = models.CharField(max_length=60, db_column='MAX_CODE', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_BILL_TIME', blank=True) # Field name made lowercase.
    dst_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_BILL_TIME', blank=True) # Field name made lowercase.
    src_bill_date = models.DateField(null=True, db_column='SRC_BILL_DATE', blank=True) # Field name made lowercase.
    dst_bill_date = models.DateField(null=True, db_column='DST_BILL_DATE', blank=True) # Field name made lowercase.
    server_id = models.IntegerField(null=True, db_column='SERVER_ID', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    succ_flag = models.IntegerField(null=True, db_column='SUCC_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDR_BILL201006'

class CdrBill201007(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    tbltype = models.IntegerField(primary_key=True, db_column='TBLTYPE') # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_SYS_PRICE', blank=True) # Field name made lowercase.
    dst_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_SYS_PRICE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    src_oper = models.IntegerField(null=True, db_column='SRC_OPER', blank=True) # Field name made lowercase.
    dst_oper = models.IntegerField(null=True, db_column='DST_OPER', blank=True) # Field name made lowercase.
    src_dest = models.IntegerField(null=True, db_column='SRC_DEST', blank=True) # Field name made lowercase.
    dst_dest = models.IntegerField(null=True, db_column='DST_DEST', blank=True) # Field name made lowercase.
    src_rid = models.IntegerField(null=True, db_column='SRC_RID', blank=True) # Field name made lowercase.
    dst_rid = models.IntegerField(null=True, db_column='DST_RID', blank=True) # Field name made lowercase.
    src_code = models.CharField(max_length=60, db_column='SRC_CODE', blank=True) # Field name made lowercase.
    dst_code = models.CharField(max_length=60, db_column='DST_CODE', blank=True) # Field name made lowercase.
    max_code = models.CharField(max_length=60, db_column='MAX_CODE', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_BILL_TIME', blank=True) # Field name made lowercase.
    dst_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_BILL_TIME', blank=True) # Field name made lowercase.
    src_bill_date = models.DateField(null=True, db_column='SRC_BILL_DATE', blank=True) # Field name made lowercase.
    dst_bill_date = models.DateField(null=True, db_column='DST_BILL_DATE', blank=True) # Field name made lowercase.
    server_id = models.IntegerField(null=True, db_column='SERVER_ID', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    succ_flag = models.IntegerField(null=True, db_column='SUCC_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDR_BILL201007'

class CdrBill201008(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    tbltype = models.IntegerField(primary_key=True, db_column='TBLTYPE') # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_SYS_PRICE', blank=True) # Field name made lowercase.
    dst_sys_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_SYS_PRICE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    src_oper = models.IntegerField(null=True, db_column='SRC_OPER', blank=True) # Field name made lowercase.
    dst_oper = models.IntegerField(null=True, db_column='DST_OPER', blank=True) # Field name made lowercase.
    src_dest = models.IntegerField(null=True, db_column='SRC_DEST', blank=True) # Field name made lowercase.
    dst_dest = models.IntegerField(null=True, db_column='DST_DEST', blank=True) # Field name made lowercase.
    src_rid = models.IntegerField(null=True, db_column='SRC_RID', blank=True) # Field name made lowercase.
    dst_rid = models.IntegerField(null=True, db_column='DST_RID', blank=True) # Field name made lowercase.
    src_code = models.CharField(max_length=60, db_column='SRC_CODE', blank=True) # Field name made lowercase.
    dst_code = models.CharField(max_length=60, db_column='DST_CODE', blank=True) # Field name made lowercase.
    max_code = models.CharField(max_length=60, db_column='MAX_CODE', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='SRC_BILL_TIME', blank=True) # Field name made lowercase.
    dst_bill_time = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='DST_BILL_TIME', blank=True) # Field name made lowercase.
    src_bill_date = models.DateField(null=True, db_column='SRC_BILL_DATE', blank=True) # Field name made lowercase.
    dst_bill_date = models.DateField(null=True, db_column='DST_BILL_DATE', blank=True) # Field name made lowercase.
    server_id = models.IntegerField(null=True, db_column='SERVER_ID', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    succ_flag = models.IntegerField(null=True, db_column='SUCC_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CDR_BILL201008'

class Cdrzero201007(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    class Meta:
        db_table = u'CDRzero201007'

class Cdrzero201008(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(primary_key=True, db_column='CID') # Field name made lowercase.
    class Meta:
        db_table = u'CDRzero201008'

class Checkcdr(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(db_column='CID') # Field name made lowercase.
    class Meta:
        db_table = u'CHECKCDR'

class CheckCdr(models.Model):
    oper = models.CharField(max_length=60, db_column='OPER', blank=True) # Field name made lowercase.
    dst_num = models.CharField(max_length=60, db_column='DST_NUM', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    conn_time = models.DateTimeField(null=True, db_column='CONN_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    peer_id = models.IntegerField(null=True, db_column='PEER_ID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='STATUS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CHECK_CDR'

class ClientsEq(models.Model):
    client_id = models.IntegerField(unique=True, null=True, db_column='CLIENT_ID', blank=True) # Field name made lowercase.
    eq_id = models.IntegerField(unique=True, null=True, db_column='EQ_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CLIENTS_EQ'

class ClientFee(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    fee_date = models.DateTimeField(null=True, db_column='FEE_DATE', blank=True) # Field name made lowercase.
    next_date = models.DateTimeField(null=True, db_column='NEXT_DATE', blank=True) # Field name made lowercase.
    summ = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='SUMM', blank=True) # Field name made lowercase.
    cause = models.CharField(max_length=135, db_column='CAUSE', blank=True) # Field name made lowercase.
    operator = models.CharField(max_length=135, db_column='OPERATOR', blank=True) # Field name made lowercase.
    freeze = models.IntegerField(null=True, db_column='FREEZE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CLIENT_FEE'

class CodesHAevstifeev(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_aevstifeev'

class CodesHApavlachev(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_apavlachev'

class CodesHAshelepin(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_ashelepin'

class CodesHAsvarichevskyy(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_asvarichevskyy'

class CodesHEklochkova(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_eklochkova'

class CodesHEsyhih(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_esyhih'

class CodesHMnakonechniy(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_mnakonechniy'

class CodesHOkhoruzhenko(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='BASE_PRICE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_okhoruzhenko'

class CodesHRaskarova(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_raskarova'

class CodesHShs(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='BASE_PRICE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_shs'

class CodesHStropanets(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='BASE_PRICE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_stropanets'

class CodesHTest(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    class Meta:
        db_table = u'CODES_H_test'

class Company(models.Model):
    address = models.CharField(max_length=450, blank=True)
    city = models.CharField(max_length=450, blank=True)
    state = models.CharField(max_length=450, blank=True)
    zip = models.CharField(max_length=450, blank=True)
    phone = models.CharField(max_length=450, blank=True)
    fax = models.CharField(max_length=450, blank=True)
    bank = models.CharField(max_length=450, blank=True)
    branch = models.CharField(max_length=450, blank=True)
    acc = models.CharField(max_length=450, blank=True)
    aba = models.CharField(max_length=450, blank=True)
    swift = models.CharField(max_length=450, blank=True)
    company_name = models.CharField(max_length=300, blank=True)
    logo = models.TextField(blank=True)
    def_field = models.IntegerField(null=True, db_column='def', blank=True) # Field renamed because it was a Python reserved word.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    inlogo = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=300, blank=True)
    iban = models.CharField(max_length=300, blank=True)
    bank_adr = models.CharField(max_length=450, blank=True)
    int_swift = models.CharField(max_length=450, blank=True)
    int_acc = models.CharField(max_length=450, blank=True)
    int_iban = models.CharField(max_length=450, blank=True)
    buh_email = models.CharField(max_length=150, blank=True)
    leader_name = models.CharField(max_length=150, blank=True)
    buh_name = models.CharField(max_length=150, blank=True)
    inn = models.CharField(max_length=450, blank=True)
    kpp = models.CharField(max_length=450, blank=True)
    bank_bik = models.CharField(max_length=450, blank=True)
    bank_acc = models.CharField(max_length=450, blank=True)
    pdf_tmpl = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'COMPANY'

class Confirm(models.Model):
    id = models.IntegerField(primary_key=True)
    guid = models.CharField(max_length=765, blank=True)
    tbl = models.CharField(max_length=60, blank=True)
    cond = models.CharField(max_length=60, blank=True)
    data = models.DateTimeField(null=True, blank=True)
    additional_info = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'CONFIRM'

class Countries(models.Model):
    country_name = models.CharField(max_length=90, db_column='COUNTRY_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    num_count = models.IntegerField(null=True, db_column='NUM_COUNT', blank=True) # Field name made lowercase.
    num_count2 = models.IntegerField(null=True, db_column='NUM_COUNT2', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'COUNTRIES'

class Currency(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=9, blank=True)
    nominal = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    class Meta:
        db_table = u'CURRENCY'

class CurrencyBase(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=9, blank=True)
    descr = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'CURRENCY_BASE'

class CurrencyRates(models.Model):
    id = models.IntegerField(primary_key=True)
    schm_id = models.IntegerField(null=True, db_column='SCHM_ID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=9, blank=True)
    nominal = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    class Meta:
        db_table = u'CURRENCY_RATES'

class Daystat(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    mera_id = models.IntegerField(null=True, db_column='MERA_ID', blank=True) # Field name made lowercase.
    orig_rate_id = models.IntegerField(null=True, db_column='ORIG_RATE_ID', blank=True) # Field name made lowercase.
    term_rate_id = models.IntegerField(null=True, db_column='TERM_RATE_ID', blank=True) # Field name made lowercase.
    sys_cost_t = models.DecimalField(null=True, max_digits=14, decimal_places=6, blank=True)
    sys_cost_o = models.DecimalField(null=True, max_digits=14, decimal_places=6, blank=True)
    stat_id = models.IntegerField(primary_key=True, db_column='STAT_ID') # Field name made lowercase.
    class Meta:
        db_table = u'DAYSTAT'

class DaystatZero(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    mera_id = models.IntegerField(null=True, db_column='MERA_ID', blank=True) # Field name made lowercase.
    orig_rate_id = models.IntegerField(null=True, db_column='ORIG_RATE_ID', blank=True) # Field name made lowercase.
    term_rate_id = models.IntegerField(null=True, db_column='TERM_RATE_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DAYSTAT_ZERO'

class Dest(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    dest_name = models.CharField(max_length=300, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    dest_codes = models.TextField(db_column='DEST_CODES', blank=True) # Field name made lowercase.
    city_name = models.CharField(max_length=150, db_column='CITY_NAME', blank=True) # Field name made lowercase.
    dest_type = models.CharField(max_length=60, db_column='DEST_TYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DEST'

class DestCode(models.Model):
    dest_id = models.IntegerField(unique=True, null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DEST_CODE'

class DestSynonym(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    dest_id = models.IntegerField(unique=True, null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(unique=True, null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=300, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DEST_SYNONYM'

class Dialonline(models.Model):
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    start_time = models.TextField(db_column='START_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    nasport = models.CharField(max_length=90, db_column='NASPORT', blank=True) # Field name made lowercase.
    nasip = models.CharField(max_length=45, db_column='NASIP', blank=True) # Field name made lowercase.
    nasid = models.CharField(max_length=90, db_column='NASID', blank=True) # Field name made lowercase.
    uid = models.IntegerField(null=True, db_column='UID', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=150, db_column='USERNAME', blank=True) # Field name made lowercase.
    rate_plan = models.IntegerField(null=True, db_column='RATE_PLAN', blank=True) # Field name made lowercase.
    framedip = models.CharField(max_length=45, db_column='FRAMEDIP', blank=True) # Field name made lowercase.
    octets_in = models.IntegerField(null=True, db_column='OCTETS_IN', blank=True) # Field name made lowercase.
    octets_out = models.IntegerField(null=True, db_column='OCTETS_OUT', blank=True) # Field name made lowercase.
    session_time = models.IntegerField(null=True, db_column='SESSION_TIME', blank=True) # Field name made lowercase.
    ani = models.CharField(max_length=75, db_column='ANI', blank=True) # Field name made lowercase.
    alive_tm = models.DateTimeField(db_column='ALIVE_TM') # Field name made lowercase.
    dnis = models.CharField(max_length=75, db_column='DNIS', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'DIALONLINE'

class DilerSale(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    diler_id = models.IntegerField(null=True, db_column='DILER_ID', blank=True) # Field name made lowercase.
    card_count = models.IntegerField(null=True, db_column='CARD_COUNT', blank=True) # Field name made lowercase.
    point_count = models.IntegerField(null=True, db_column='POINT_COUNT', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='PRICE', blank=True) # Field name made lowercase.
    sale_date = models.DateField(null=True, db_column='SALE_DATE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    serial_from = models.IntegerField(null=True, db_column='SERIAL_FROM', blank=True) # Field name made lowercase.
    serial_to = models.IntegerField(null=True, db_column='SERIAL_TO', blank=True) # Field name made lowercase.
    sale_type = models.IntegerField(null=True, db_column='SALE_TYPE', blank=True) # Field name made lowercase.
    lot_id = models.IntegerField(null=True, db_column='LOT_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DILER_SALE'

class DublId(models.Model):
    id = models.BigIntegerField(null=True, db_column='ID', blank=True) # Field name made lowercase.
    cnt = models.BigIntegerField()
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DUBL_ID'

class ExcludeDates(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    tz_id = models.IntegerField(unique=True, null=True, db_column='TZ_ID', blank=True) # Field name made lowercase.
    year = models.IntegerField(unique=True, null=True, db_column='YEAR', blank=True) # Field name made lowercase.
    month = models.IntegerField(unique=True, null=True, db_column='MONTH', blank=True) # Field name made lowercase.
    day = models.IntegerField(unique=True, null=True, db_column='DAY', blank=True) # Field name made lowercase.
    date_flag = models.IntegerField(unique=True, null=True, db_column='DATE_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'EXCLUDE_DATES'

class Fixpays(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    fix_month = models.IntegerField(null=True, db_column='FIX_MONTH', blank=True) # Field name made lowercase.
    fix_year = models.IntegerField(null=True, db_column='FIX_YEAR', blank=True) # Field name made lowercase.
    prihod = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    rashod = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    class Meta:
        db_table = u'FIXPAYS'

class Flags(models.Model):
    flag_id = models.IntegerField(primary_key=True, db_column='FLAG_ID') # Field name made lowercase.
    flag_name = models.CharField(max_length=75, db_column='FLAG_NAME', blank=True) # Field name made lowercase.
    flag_value = models.IntegerField(null=True, db_column='FLAG_VALUE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'FLAGS'

class Forms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    f_alias = models.CharField(max_length=150, db_column='F_ALIAS', blank=True) # Field name made lowercase.
    menu_id = models.IntegerField(null=True, db_column='MENU_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'FORMS'

class ForwardRules(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    client_id = models.IntegerField(null=True, db_column='CLIENT_ID', blank=True) # Field name made lowercase.
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    forward_number = models.CharField(max_length=60, db_column='FORWARD_NUMBER', blank=True) # Field name made lowercase.
    start_date = models.DateTimeField(unique=True, db_column='START_DATE') # Field name made lowercase.
    stop_date = models.DateTimeField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    user = models.CharField(max_length=60, blank=True)
    cause = models.IntegerField(null=True, db_column='CAUSE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'FORWARD_RULES'

class Gateways(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    gate_id = models.CharField(unique=True, max_length=60, db_column='GATE_ID', blank=True) # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP', blank=True) # Field name made lowercase.
    proxy_type = models.IntegerField(null=True, db_column='PROXY_TYPE', blank=True) # Field name made lowercase.
    serv_id = models.IntegerField(unique=True, null=True, db_column='SERV_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'GATEWAYS'

class HotStat(models.Model):
    conf_id = models.CharField(max_length=150, db_column='CONF_ID', blank=True) # Field name made lowercase.
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    aon = models.IntegerField(null=True, db_column='AON', blank=True) # Field name made lowercase.
    pin = models.IntegerField(null=True, db_column='PIN', blank=True) # Field name made lowercase.
    result = models.IntegerField(null=True, db_column='RESULT', blank=True) # Field name made lowercase.
    term_id = models.IntegerField(null=True, db_column='TERM_ID', blank=True) # Field name made lowercase.
    tarif = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TARIF', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='PRICE', blank=True) # Field name made lowercase.
    ses_time = models.IntegerField(null=True, db_column='SES_TIME', blank=True) # Field name made lowercase.
    round_time = models.IntegerField(null=True, db_column='ROUND_TIME', blank=True) # Field name made lowercase.
    dest = models.CharField(max_length=60, db_column='DEST', blank=True) # Field name made lowercase.
    aon_n = models.CharField(max_length=60, db_column='AON_N', blank=True) # Field name made lowercase.
    pin_n = models.CharField(max_length=60, db_column='PIN_N', blank=True) # Field name made lowercase.
    conn_flag = models.IntegerField(null=True, db_column='CONN_FLAG', blank=True) # Field name made lowercase.
    dnis = models.CharField(max_length=90, db_column='DNIS', blank=True) # Field name made lowercase.
    start_time = models.TextField(db_column='START_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    nas_ip = models.CharField(max_length=45, db_column='NAS_IP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'HOT_STAT'

class Hourstat(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(primary_key=True, db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HOURSTAT'

class HourstatBuf(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(primary_key=True, db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HOURSTAT_BUF'

class HsHAevstifeev(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_aevstifeev'

class HsHApavlachev(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_apavlachev'

class HsHAshelepin(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_ashelepin'

class HsHAsvarichevskyy(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_asvarichevskyy'

class HsHEklochkova(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_eklochkova'

class HsHEsyhih(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_esyhih'

class HsHMnakonechniy(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_mnakonechniy'

class HsHOkhoruzhenko(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_okhoruzhenko'

class HsHRaskarova(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_raskarova'

class HsHShs(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_shs'

class HsHStropanets(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_stropanets'

class HsHTest(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    vhour = models.IntegerField(null=True, db_column='VHOUR', blank=True) # Field name made lowercase.
    term_oper_id = models.IntegerField(null=True, db_column='TERM_OPER_ID', blank=True) # Field name made lowercase.
    orig_oper_id = models.IntegerField(null=True, db_column='ORIG_OPER_ID', blank=True) # Field name made lowercase.
    term_dest_id = models.IntegerField(null=True, db_column='TERM_DEST_ID', blank=True) # Field name made lowercase.
    orig_dest_id = models.IntegerField(null=True, db_column='ORIG_DEST_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    term_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TERM_COST', blank=True) # Field name made lowercase.
    orig_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ORIG_COST', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=30, db_column='CODE', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    hid = models.IntegerField(db_column='HID') # Field name made lowercase.
    class Meta:
        db_table = u'HS_H_test'

class IncludePer(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    date_tm_id = models.IntegerField(unique=True, null=True, db_column='DATE_TM_ID', blank=True) # Field name made lowercase.
    day = models.IntegerField(unique=True, null=True, db_column='DAY', blank=True) # Field name made lowercase.
    from_tm = models.IntegerField(unique=True, null=True, db_column='FROM_TM', blank=True) # Field name made lowercase.
    to_tm = models.IntegerField(unique=True, null=True, db_column='TO_TM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'INCLUDE_PER'

class InetIf(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    ifindex = models.IntegerField(null=True, db_column='IFindex', blank=True) # Field name made lowercase.
    eq_id = models.IntegerField(null=True, db_column='EQ_ID', blank=True) # Field name made lowercase.
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, db_column='STATE', blank=True) # Field name made lowercase.
    ifname = models.CharField(max_length=768, db_column='IFname', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'INET_IF'

class InetIp(models.Model):
    site_id = models.IntegerField(db_column='SITE_ID') # Field name made lowercase.
    oper_ip = models.CharField(unique=True, max_length=45, db_column='OPER_IP', blank=True) # Field name made lowercase.
    bit_mask = models.BigIntegerField(null=True, db_column='BIT_MASK', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    eq_id = models.IntegerField(null=True, db_column='EQ_ID', blank=True) # Field name made lowercase.
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, db_column='STATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'INET_IP'

class InvHistory(models.Model):
    inv_id = models.IntegerField(primary_key=True, db_column='INV_ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    inv_date = models.DateField(null=True, db_column='INV_DATE', blank=True) # Field name made lowercase.
    inv_sum = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='INV_SUM', blank=True) # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    currency = models.CharField(max_length=9, db_column='CURRENCY', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='STATUS', blank=True) # Field name made lowercase.
    send_mail = models.CharField(max_length=765, db_column='SEND_MAIL', blank=True) # Field name made lowercase.
    inv_file = models.CharField(max_length=600, db_column='INV_FILE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'INV_HISTORY'

class IpList(models.Model):
    net_id = models.IntegerField(null=True, db_column='NET_ID', blank=True) # Field name made lowercase.
    net_ip = models.BigIntegerField(unique=True, null=True, db_column='NET_IP', blank=True) # Field name made lowercase.
    bit_mask = models.BigIntegerField(null=True, db_column='BIT_MASK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IP_LIST'

class Infmail(models.Model):
    mailid = models.IntegerField(primary_key=True, db_column='MailID') # Field name made lowercase.
    sender = models.CharField(max_length=765, db_column='Sender', blank=True) # Field name made lowercase.
    reciever = models.CharField(max_length=765, db_column='Reciever', blank=True) # Field name made lowercase.
    maildate = models.DateField(null=True, db_column='MailDate', blank=True) # Field name made lowercase.
    mailbody = models.TextField(db_column='MailBody', blank=True) # Field name made lowercase.
    theme = models.CharField(max_length=765, db_column='Theme', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'InfMail'

class Langs(models.Model):
    lang = models.CharField(max_length=9, primary_key=True, db_column='LANG') # Field name made lowercase.
    class Meta:
        db_table = u'LANGS'

class LoadedNf(models.Model):
    filename = models.CharField(max_length=600, primary_key=True, db_column='FILENAME') # Field name made lowercase.
    arch_flag = models.IntegerField(null=True, db_column='ARCH_FLAG', blank=True) # Field name made lowercase.
    rm_flag = models.IntegerField(null=True, db_column='RM_FLAG', blank=True) # Field name made lowercase.
    ldate = models.DateTimeField(db_column='LDATE') # Field name made lowercase.
    class Meta:
        db_table = u'LOADED_NF'

class Logs(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    logdate = models.DateField(null=True, db_column='LOGDATE', blank=True) # Field name made lowercase.
    logtime = models.TextField(db_column='LOGTIME', blank=True) # Field name made lowercase. This field type is a guess.
    form_id = models.IntegerField(null=True, db_column='FORM_ID', blank=True) # Field name made lowercase.
    action_id = models.IntegerField(null=True, db_column='ACTION_ID', blank=True) # Field name made lowercase.
    filename = models.CharField(max_length=300, db_column='FILENAME', blank=True) # Field name made lowercase.
    logstr = models.TextField(db_column='LOGSTR', blank=True) # Field name made lowercase.
    file = models.TextField(db_column='FILE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOGS'

class Lots(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(unique=True, max_length=150, db_column='NAME', blank=True) # Field name made lowercase.
    rate_plan = models.IntegerField(null=True, db_column='RATE_PLAN', blank=True) # Field name made lowercase.
    diler = models.IntegerField(null=True, db_column='DILER', blank=True) # Field name made lowercase.
    prefix = models.CharField(max_length=90, db_column='PREFIX', blank=True) # Field name made lowercase.
    serial_start = models.IntegerField(null=True, db_column='SERIAL_START', blank=True) # Field name made lowercase.
    date_create = models.DateField(null=True, db_column='DATE_CREATE', blank=True) # Field name made lowercase.
    cards_count = models.IntegerField(null=True, db_column='CARDS_COUNT', blank=True) # Field name made lowercase.
    date_use = models.DateField(null=True, db_column='DATE_USE', blank=True) # Field name made lowercase.
    period_use = models.IntegerField(null=True, db_column='PERIOD_USE', blank=True) # Field name made lowercase.
    type_use = models.IntegerField(null=True, db_column='TYPE_USE', blank=True) # Field name made lowercase.
    period_active = models.IntegerField(null=True, db_column='PERIOD_ACTIVE', blank=True) # Field name made lowercase.
    type_active = models.IntegerField(null=True, db_column='TYPE_ACTIVE', blank=True) # Field name made lowercase.
    pin_len = models.IntegerField(null=True, db_column='PIN_LEN', blank=True) # Field name made lowercase.
    key_len = models.IntegerField(null=True, db_column='KEY_LEN', blank=True) # Field name made lowercase.
    surch_plan = models.IntegerField(null=True, db_column='SURCH_PLAN', blank=True) # Field name made lowercase.
    dnis = models.IntegerField(null=True, db_column='DNIS', blank=True) # Field name made lowercase.
    rp_flag = models.IntegerField(null=True, db_column='RP_FLAG', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, db_column='STATE', blank=True) # Field name made lowercase.
    period_charge = models.IntegerField(null=True, db_column='PERIOD_CHARGE', blank=True) # Field name made lowercase.
    type_charge = models.IntegerField(null=True, db_column='TYPE_CHARGE', blank=True) # Field name made lowercase.
    subcharge = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SUBCHARGE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOTS'

class LotPref(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    lot_id = models.IntegerField(unique=True, null=True, db_column='LOT_ID', blank=True) # Field name made lowercase.
    prefix = models.CharField(max_length=30, db_column='PREFIX', blank=True) # Field name made lowercase.
    inprefix = models.CharField(max_length=765, db_column='INPREFIX', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LOT_PREF'

class Managers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='NAME', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=300, db_column='EMAIL', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=60, db_column='PHONE', blank=True) # Field name made lowercase.
    type = models.IntegerField(null=True, db_column='TYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MANAGERS'

class ManualCurrency(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=9, blank=True)
    nominal = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    class Meta:
        db_table = u'MANUAL_CURRENCY'

class Menus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    menu_alias = models.CharField(max_length=150, db_column='MENU_ALIAS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MENUS'

class MeraLog(models.Model):
    host = models.CharField(max_length=45, db_column='HOST', blank=True) # Field name made lowercase.
    log = models.TextField(db_column='LOG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MERA_LOG'

class Mvtsonline(models.Model):
    icid = models.IntegerField(unique=True, null=True, db_column='ICID', blank=True) # Field name made lowercase.
    host = models.CharField(unique=True, max_length=45, db_column='HOST', blank=True) # Field name made lowercase.
    number_in = models.CharField(max_length=90, db_column='NUMBER_IN', blank=True) # Field name made lowercase.
    number_out = models.CharField(max_length=90, db_column='NUMBER_OUT', blank=True) # Field name made lowercase.
    ip_in = models.CharField(max_length=45, db_column='IP_IN', blank=True) # Field name made lowercase.
    ip_out = models.CharField(max_length=45, db_column='IP_OUT', blank=True) # Field name made lowercase.
    talk_time = models.IntegerField(null=True, db_column='TALK_TIME', blank=True) # Field name made lowercase.
    bytes_in_src = models.IntegerField(null=True, db_column='BYTES_IN_SRC', blank=True) # Field name made lowercase.
    bytes_out_src = models.IntegerField(null=True, db_column='BYTES_OUT_SRC', blank=True) # Field name made lowercase.
    bytes_in_dst = models.IntegerField(null=True, db_column='BYTES_IN_DST', blank=True) # Field name made lowercase.
    bytes_out_dst = models.IntegerField(null=True, db_column='BYTES_OUT_DST', blank=True) # Field name made lowercase.
    in_proto = models.CharField(max_length=60, db_column='IN_PROTO', blank=True) # Field name made lowercase.
    out_proto = models.CharField(max_length=60, db_column='OUT_PROTO', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'MVTSONLINE'

class NetflowStat(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    src_oper_id = models.IntegerField(null=True, db_column='SRC_OPER_ID', blank=True) # Field name made lowercase.
    dst_oper_id = models.IntegerField(null=True, db_column='DST_OPER_ID', blank=True) # Field name made lowercase.
    src_dest_id = models.IntegerField(null=True, db_column='SRC_DEST_ID', blank=True) # Field name made lowercase.
    dst_dest_id = models.IntegerField(null=True, db_column='DST_DEST_ID', blank=True) # Field name made lowercase.
    bytes = models.BigIntegerField(null=True, db_column='BYTES', blank=True) # Field name made lowercase.
    src_price = models.DecimalField(decimal_places=5, null=True, max_digits=16, db_column='SRC_PRICE', blank=True) # Field name made lowercase.
    dst_price = models.DecimalField(decimal_places=5, null=True, max_digits=16, db_column='DST_PRICE', blank=True) # Field name made lowercase.
    src_cost = models.DecimalField(decimal_places=11, null=True, max_digits=22, db_column='SRC_COST', blank=True) # Field name made lowercase.
    dst_cost = models.DecimalField(decimal_places=11, null=True, max_digits=22, db_column='DST_COST', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    bill_hour = models.IntegerField(null=True, db_column='BILL_HOUR', blank=True) # Field name made lowercase.
    bill_hash = models.CharField(unique=True, max_length=120, db_column='BILL_HASH', blank=True) # Field name made lowercase.
    src_rate = models.IntegerField(null=True, db_column='SRC_RATE', blank=True) # Field name made lowercase.
    dst_rate = models.IntegerField(null=True, db_column='DST_RATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'NETFLOW_STAT'

class NetworkList(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    net_alias = models.CharField(unique=True, max_length=90, db_column='NET_ALIAS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'NETWORK_LIST'

class Onlinestat(models.Model):
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(unique=True, null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(unique=True, null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    dest = models.IntegerField(unique=True, null=True, db_column='DEST', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ONLINESTAT'

class OperAni(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    set_id = models.IntegerField(unique=True, null=True, db_column='SET_ID', blank=True) # Field name made lowercase.
    ani_id = models.IntegerField(unique=True, null=True, db_column='ANI_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'OPER_ANI'

class OperFee(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    rate_fee_id = models.IntegerField(null=True, db_column='RATE_FEE_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'OPER_FEE'

class Pay(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    pay_date = models.DateField(null=True, db_column='PAY_DATE', blank=True) # Field name made lowercase.
    db_date = models.DateField(null=True, db_column='DB_DATE', blank=True) # Field name made lowercase.
    pay_sum = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='PAY_SUM', blank=True) # Field name made lowercase.
    pay_fact = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='PAY_FACT', blank=True) # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    pay_type = models.IntegerField(null=True, db_column='PAY_TYPE', blank=True) # Field name made lowercase.
    comment = models.CharField(max_length=765, db_column='COMMENT', blank=True) # Field name made lowercase.
    db_time = models.TextField(db_column='DB_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    cur_name = models.CharField(max_length=15, db_column='CUR_NAME', blank=True) # Field name made lowercase.
    exch_rate = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='EXCH_RATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PAY'

class PayTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, blank=True)
    pay_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'PAY_TYPES'

class PersonCard(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    fname = models.CharField(max_length=90, db_column='FNAME', blank=True) # Field name made lowercase.
    sname = models.CharField(max_length=120, db_column='SNAME', blank=True) # Field name made lowercase.
    mname = models.CharField(max_length=90, db_column='MNAME', blank=True) # Field name made lowercase.
    orgname = models.CharField(max_length=150, db_column='ORGNAME', blank=True) # Field name made lowercase.
    contract = models.CharField(max_length=60, db_column='CONTRACT', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=90, db_column='PHONE', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=90, db_column='EMAIL', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PERSON_CARD'

class Prefix(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(unique=True, null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    prefix = models.CharField(unique=True, max_length=30, db_column='PREFIX', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'PREFIX'

class Pstack(models.Model):
    oper_id = models.IntegerField(unique=True, null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    period = models.CharField(unique=True, max_length=765, db_column='PERIOD', blank=True) # Field name made lowercase.
    iplist = models.TextField(unique=True, db_column='IPLIST', blank=True) # Field name made lowercase.
    proc_id = models.IntegerField(null=True, db_column='PROC_ID', blank=True) # Field name made lowercase.
    mindate = models.DateField(unique=True, null=True, db_column='MINDATE', blank=True) # Field name made lowercase.
    maxdate = models.DateField(unique=True, null=True, db_column='MAXDATE', blank=True) # Field name made lowercase.
    ruser = models.CharField(max_length=150, db_column='RUSER', blank=True) # Field name made lowercase.
    pos = models.IntegerField(primary_key=True, db_column='POS') # Field name made lowercase.
    class Meta:
        db_table = u'PSTACK'

class QCode(models.Model):
    id = models.IntegerField(null=True, db_column='ID', blank=True) # Field name made lowercase.
    descr = models.CharField(max_length=765, db_column='DESCR', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Q_CODE'

class Radonline(models.Model):
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=120, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=120, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=90, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=120, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=120, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=90, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=45, db_column='DST_IP', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=45, db_column='SRC_IP', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    auth_time = models.DateTimeField(db_column='AUTH_TIME') # Field name made lowercase.
    host = models.CharField(max_length=45, db_column='HOST', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=75, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=75, db_column='DST_USER', blank=True) # Field name made lowercase.
    rid_o = models.IntegerField(null=True, db_column='RID_O', blank=True) # Field name made lowercase.
    rid_t = models.IntegerField(null=True, db_column='RID_T', blank=True) # Field name made lowercase.
    rgrp_id_o = models.IntegerField(null=True, db_column='RGRP_ID_O', blank=True) # Field name made lowercase.
    rgrp_id_t = models.IntegerField(null=True, db_column='RGRP_ID_T', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=90, db_column='CODE', blank=True) # Field name made lowercase.
    src_site = models.IntegerField(null=True, db_column='SRC_SITE', blank=True) # Field name made lowercase.
    dst_site = models.IntegerField(null=True, db_column='DST_SITE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RADONLINE'

class Rates(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code_id = models.IntegerField(null=True, db_column='CODE_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(unique=True, null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    time_id = models.IntegerField(null=True, db_column='TIME_ID', blank=True) # Field name made lowercase.
    round_id = models.IntegerField(null=True, db_column='ROUND_ID', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    minsec = models.IntegerField(null=True, blank=True)
    unpaidsec = models.IntegerField(null=True, blank=True)
    discr_sec = models.IntegerField(null=True, blank=True)
    round_sec = models.IntegerField(null=True, blank=True)
    from_tm = models.IntegerField(null=True, blank=True)
    to_tm = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    fround = models.IntegerField(null=True, blank=True)
    ncnt = models.IntegerField(null=True, blank=True)
    close_hour = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    grp = models.IntegerField(null=True, db_column='GRP', blank=True) # Field name made lowercase.
    deny_grp = models.IntegerField(null=True, db_column='DENY_GRP', blank=True) # Field name made lowercase.
    tz_id = models.IntegerField(unique=True, null=True, db_column='TZ_ID', blank=True) # Field name made lowercase.
    db_date = models.DateTimeField(db_column='DB_DATE') # Field name made lowercase.
    fee_limit = models.BigIntegerField(unique=True, null=True, db_column='FEE_LIMIT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES'

class RatesHAevstifeev(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_aevstifeev'

class RatesHApavlachev(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_apavlachev'

class RatesHAshelepin(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_ashelepin'

class RatesHAsvarichevskyy(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_asvarichevskyy'

class RatesHEklochkova(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_eklochkova'

class RatesHEsyhih(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_esyhih'

class RatesHMnakonechniy(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_mnakonechniy'

class RatesHOkhoruzhenko(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='BASE_PRICE', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_okhoruzhenko'

class RatesHRaskarova(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_raskarova'

class RatesHShs(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='BASE_PRICE', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_shs'

class RatesHStropanets(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='BASE_PRICE', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_stropanets'

class RatesHTest(models.Model):
    dest_id = models.IntegerField(null=True, db_column='DEST_ID', blank=True) # Field name made lowercase.
    dest_name = models.CharField(max_length=453, db_column='DEST_NAME', blank=True) # Field name made lowercase.
    country_code = models.CharField(max_length=30, db_column='COUNTRY_CODE', blank=True) # Field name made lowercase.
    code = models.CharField(max_length=60, db_column='CODE', blank=True) # Field name made lowercase.
    base_price = models.IntegerField(db_column='BASE_PRICE') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=10, null=True, max_digits=18, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=8, null=True, max_digits=40, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.DecimalField(decimal_places=0, null=True, max_digits=33, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_H_test'

class RatesLoadTmp(models.Model):
    sdate = models.DateField(null=True, blank=True)
    line = models.TextField(blank=True)
    class Meta:
        db_table = u'RATES_LOAD_TMP'

class RatesLog(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    code_id = models.IntegerField(null=True, db_column='CODE_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateTimeField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    time_id = models.IntegerField(null=True, db_column='TIME_ID', blank=True) # Field name made lowercase.
    round_id = models.IntegerField(null=True, db_column='ROUND_ID', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    minsec = models.IntegerField(null=True, blank=True)
    unpaidsec = models.IntegerField(null=True, blank=True)
    discr_sec = models.IntegerField(null=True, blank=True)
    round_sec = models.IntegerField(null=True, blank=True)
    from_tm = models.IntegerField(null=True, blank=True)
    to_tm = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    operator = models.CharField(max_length=60, blank=True)
    action = models.CharField(max_length=30, blank=True)
    logdate = models.DateTimeField(db_column='LOGDATE') # Field name made lowercase.
    fround = models.IntegerField(null=True, blank=True)
    ncnt = models.IntegerField(null=True, blank=True)
    tz_id = models.IntegerField(null=True, db_column='TZ_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_LOG'

class RatesOld(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code_id = models.IntegerField(null=True, db_column='CODE_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(unique=True, null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    time_id = models.IntegerField(null=True, db_column='TIME_ID', blank=True) # Field name made lowercase.
    round_id = models.IntegerField(null=True, db_column='ROUND_ID', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    minsec = models.IntegerField(null=True, blank=True)
    unpaidsec = models.IntegerField(null=True, blank=True)
    discr_sec = models.IntegerField(null=True, blank=True)
    round_sec = models.IntegerField(null=True, blank=True)
    from_tm = models.IntegerField(null=True, blank=True)
    to_tm = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    fround = models.IntegerField(null=True, blank=True)
    ncnt = models.IntegerField(null=True, blank=True)
    close_hour = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    grp = models.IntegerField(null=True, db_column='GRP', blank=True) # Field name made lowercase.
    deny_grp = models.IntegerField(null=True, db_column='DENY_GRP', blank=True) # Field name made lowercase.
    tz_id = models.IntegerField(unique=True, null=True, db_column='TZ_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATES_OLD'

class RatesTmp(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    code_id = models.IntegerField(null=True, db_column='CODE_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='PRICE', blank=True) # Field name made lowercase.
    rate_date = models.DateTimeField(null=True, db_column='RATE_DATE', blank=True) # Field name made lowercase.
    time_id = models.IntegerField(null=True, db_column='TIME_ID', blank=True) # Field name made lowercase.
    round_id = models.IntegerField(null=True, db_column='ROUND_ID', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    minsec = models.IntegerField(null=True, blank=True)
    unpaidsec = models.IntegerField(null=True, blank=True)
    discr_sec = models.IntegerField(null=True, blank=True)
    round_sec = models.IntegerField(null=True, blank=True)
    from_tm = models.IntegerField(null=True, blank=True)
    to_tm = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'RATES_TMP'

class RateChangeHist(models.Model):
    client_id = models.IntegerField(unique=True, null=True, db_column='CLIENT_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    start_date = models.DateField(unique=True, null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATE_CHANGE_HIST'

class RateFee(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    fee_calc_id = models.IntegerField(null=True, db_column='FEE_CALC_ID', blank=True) # Field name made lowercase.
    limit = models.BigIntegerField(null=True, db_column='LIMIT', blank=True) # Field name made lowercase.
    fee_amount = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='FEE_AMOUNT', blank=True) # Field name made lowercase.
    start_date = models.DateTimeField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    stop_date = models.DateTimeField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    next_rate_id = models.IntegerField(null=True, db_column='NEXT_RATE_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATE_FEE'

class RateFeeCalcs(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=135, db_column='NAME') # Field name made lowercase.
    proc_name = models.CharField(max_length=450, db_column='PROC_NAME') # Field name made lowercase.
    descript = models.CharField(max_length=765, db_column='DESCRIPT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATE_FEE_CALCS'

class RateNames(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    ratename = models.CharField(max_length=384, db_column='RATENAME', blank=True) # Field name made lowercase.
    minsec = models.IntegerField(null=True, blank=True)
    unpaidsec = models.IntegerField(null=True, blank=True)
    discr_sec = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, db_column='TYPE', blank=True) # Field name made lowercase.
    subpay = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='SUBPAY', blank=True) # Field name made lowercase.
    currency = models.CharField(max_length=9, db_column='CURRENCY', blank=True) # Field name made lowercase.
    last_date = models.DateField(null=True, db_column='LAST_DATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RATE_NAMES'

class RetailClients(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='NAME', blank=True) # Field name made lowercase.
    parent_id = models.IntegerField(null=True, db_column='PARENT_ID', blank=True) # Field name made lowercase.
    orig_rate = models.IntegerField(null=True, db_column='ORIG_RATE', blank=True) # Field name made lowercase.
    uid = models.IntegerField(null=True, db_column='UID', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    alias = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'RETAIL_CLIENTS'

class RetailDilers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='NAME', blank=True) # Field name made lowercase.
    parent_id = models.IntegerField(null=True, db_column='PARENT_ID', blank=True) # Field name made lowercase.
    orig_rate = models.IntegerField(null=True, db_column='ORIG_RATE', blank=True) # Field name made lowercase.
    uid = models.IntegerField(null=True, db_column='UID', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RETAIL_DILERS'

class RetStat(models.Model):
    call_id = models.CharField(max_length=150, db_column='CALL_ID', blank=True) # Field name made lowercase.
    start_time = models.DateTimeField(null=True, db_column='START_TIME', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=150, db_column='SRC_USER', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=48, db_column='SRC_IP', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=48, db_column='DST_IP', blank=True) # Field name made lowercase.
    tarif = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TARIF', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='PRICE', blank=True) # Field name made lowercase.
    ses_time = models.IntegerField(null=True, db_column='SES_TIME', blank=True) # Field name made lowercase.
    round_time = models.IntegerField(null=True, db_column='ROUND_TIME', blank=True) # Field name made lowercase.
    dst_number = models.CharField(max_length=60, db_column='DST_NUMBER', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    result = models.IntegerField(null=True, db_column='RESULT', blank=True) # Field name made lowercase.
    res_str = models.CharField(max_length=765, db_column='RES_STR', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RET_STAT'

class Rights(models.Model):
    act_id = models.IntegerField(unique=True, null=True, db_column='ACT_ID', blank=True) # Field name made lowercase.
    frm_id = models.IntegerField(unique=True, null=True, db_column='FRM_ID', blank=True) # Field name made lowercase.
    grp_id = models.IntegerField(unique=True, null=True, db_column='GRP_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RIGHTS'

class RoamingCalls(models.Model):
    cid = models.IntegerField(unique=True, db_column='CID') # Field name made lowercase.
    client_id = models.IntegerField(null=True, db_column='CLIENT_ID', blank=True) # Field name made lowercase.
    client_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='CLIENT_COST', blank=True) # Field name made lowercase.
    client_rate = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='CLIENT_RATE', blank=True) # Field name made lowercase.
    tm = models.CharField(unique=True, max_length=3, db_column='TM', blank=True) # Field name made lowercase.
    bill_date = models.DateField(unique=True, null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ROAMING_CALLS'

class RoamingClients(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    login = models.CharField(unique=True, max_length=60, db_column='LOGIN', blank=True) # Field name made lowercase.
    fio = models.CharField(max_length=180, db_column='FIO', blank=True) # Field name made lowercase.
    balance = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='BALANCE', blank=True) # Field name made lowercase.
    max_credit = models.IntegerField(null=True, db_column='MAX_CREDIT', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ROAMING_CLIENTS'

class RoamPay(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    client_id = models.IntegerField(null=True, db_column='CLIENT_ID', blank=True) # Field name made lowercase.
    summ = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SUMM', blank=True) # Field name made lowercase.
    paydate = models.DateField(null=True, db_column='PAYDATE', blank=True) # Field name made lowercase.
    dbdate = models.DateTimeField(db_column='DBDATE') # Field name made lowercase.
    cause = models.CharField(max_length=765, db_column='CAUSE', blank=True) # Field name made lowercase.
    pay_type = models.IntegerField(null=True, db_column='PAY_TYPE', blank=True) # Field name made lowercase.
    oper = models.CharField(max_length=150, db_column='OPER', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ROAM_PAY'

class Roumstat(models.Model):
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    sale_oper_id = models.IntegerField(null=True, db_column='SALE_OPER_ID', blank=True) # Field name made lowercase.
    buy_oper_id = models.IntegerField(null=True, db_column='BUY_OPER_ID', blank=True) # Field name made lowercase.
    sale_rate_id = models.IntegerField(null=True, db_column='SALE_RATE_ID', blank=True) # Field name made lowercase.
    buy_rate_id = models.IntegerField(null=True, db_column='BUY_RATE_ID', blank=True) # Field name made lowercase.
    sale_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SALE_COST', blank=True) # Field name made lowercase.
    buy_cost = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='BUY_COST', blank=True) # Field name made lowercase.
    sale_abon = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SALE_ABON', blank=True) # Field name made lowercase.
    buy_abon = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='BUY_ABON', blank=True) # Field name made lowercase.
    all_min = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ALL_MIN', blank=True) # Field name made lowercase.
    all_calls = models.IntegerField(null=True, db_column='ALL_CALLS', blank=True) # Field name made lowercase.
    succ_calls = models.IntegerField(null=True, db_column='SUCC_CALLS', blank=True) # Field name made lowercase.
    short_calls = models.IntegerField(null=True, db_column='SHORT_CALLS', blank=True) # Field name made lowercase.
    compl_calls = models.IntegerField(null=True, db_column='COMPL_CALLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ROUMSTAT'

class Roundes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    unpaid_time = models.IntegerField(null=True, db_column='UNPAID_TIME', blank=True) # Field name made lowercase.
    round = models.IntegerField(null=True, db_column='ROUND', blank=True) # Field name made lowercase.
    step = models.IntegerField(null=True, db_column='STEP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ROUNDES'

class RouteGroups(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    gname = models.CharField(unique=True, max_length=300, db_column='GNAME', blank=True) # Field name made lowercase.
    gdesc = models.TextField(db_column='GDESC', blank=True) # Field name made lowercase.
    ginclude = models.CharField(max_length=765, db_column='GINCLUDE', blank=True) # Field name made lowercase.
    client_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='CLIENT_PRICE', blank=True) # Field name made lowercase.
    carrier_price = models.DecimalField(decimal_places=6, null=True, max_digits=16, db_column='CARRIER_PRICE', blank=True) # Field name made lowercase.
    transit_flag = models.IntegerField(null=True, db_column='TRANSIT_FLAG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ROUTE_GROUPS'

class Rplans(models.Model):
    rp_id = models.IntegerField(unique=True, null=True, db_column='RP_ID', blank=True) # Field name made lowercase.
    rate_id = models.IntegerField(null=True, db_column='RATE_ID', blank=True) # Field name made lowercase.
    dnis_id = models.IntegerField(unique=True, null=True, db_column='DNIS_ID', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    ani_id = models.IntegerField(unique=True, null=True, db_column='ANI_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RPLANS'

class RpNames(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rp_name = models.CharField(max_length=300, db_column='RP_NAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'RP_NAMES'

class SchemeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True)
    data = models.DateTimeField(null=True, blank=True)
    defvalute = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'SCHEME_INFO'

class Servers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    server_name = models.CharField(unique=True, max_length=90, db_column='SERVER_NAME', blank=True) # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP', blank=True) # Field name made lowercase.
    ftp_login = models.CharField(max_length=60, db_column='FTP_LOGIN', blank=True) # Field name made lowercase.
    ftp_pass = models.CharField(max_length=60, db_column='FTP_PASS', blank=True) # Field name made lowercase.
    me = models.IntegerField(null=True, db_column='ME', blank=True) # Field name made lowercase.
    radius_ip = models.CharField(max_length=45, db_column='RADIUS_IP', blank=True) # Field name made lowercase.
    radius_port = models.IntegerField(null=True, db_column='RADIUS_PORT', blank=True) # Field name made lowercase.
    radius_key = models.CharField(max_length=60, db_column='RADIUS_KEY', blank=True) # Field name made lowercase.
    en_radius = models.IntegerField(null=True, db_column='EN_RADIUS', blank=True) # Field name made lowercase.
    en_acct = models.IntegerField(null=True, db_column='EN_ACCT', blank=True) # Field name made lowercase.
    local_acct_port = models.IntegerField(null=True, db_column='LOCAL_ACCT_PORT', blank=True) # Field name made lowercase.
    local_auth_port = models.IntegerField(null=True, db_column='LOCAL_AUTH_PORT', blank=True) # Field name made lowercase.
    acct_port = models.IntegerField(null=True, db_column='ACCT_PORT', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    protocol = models.IntegerField(null=True, blank=True)
    route_port = models.IntegerField(null=True, db_column='ROUTE_PORT', blank=True) # Field name made lowercase.
    local_route_port = models.IntegerField(null=True, db_column='LOCAL_ROUTE_PORT', blank=True) # Field name made lowercase.
    p_type = models.IntegerField(null=True, db_column='P_TYPE', blank=True) # Field name made lowercase.
    s_type = models.IntegerField(null=True, db_column='S_TYPE', blank=True) # Field name made lowercase.
    time_name = models.CharField(max_length=45, blank=True)
    time_offset = models.CharField(max_length=45, blank=True)
    moniport = models.IntegerField(null=True, db_column='MONIPORT', blank=True) # Field name made lowercase.
    monipass = models.CharField(max_length=150, db_column='MONIPASS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SERVERS'

class SessParam(models.Model):
    sess_id = models.IntegerField(primary_key=True, db_column='SESS_ID') # Field name made lowercase.
    conf_id = models.CharField(max_length=150, db_column='CONF_ID', blank=True) # Field name made lowercase.
    tarif = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='TARIF', blank=True) # Field name made lowercase.
    uid = models.IntegerField(null=True, db_column='UID', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    min_amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='MIN_AMOUNT', blank=True) # Field name made lowercase.
    category = models.IntegerField(null=True, db_column='CATEGORY', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    round_time = models.IntegerField(null=True, db_column='ROUND_TIME', blank=True) # Field name made lowercase.
    min_time = models.IntegerField(null=True, db_column='MIN_TIME', blank=True) # Field name made lowercase.
    step_time = models.IntegerField(null=True, db_column='STEP_TIME', blank=True) # Field name made lowercase.
    technology = models.IntegerField(null=True, db_column='TECHNOLOGY', blank=True) # Field name made lowercase.
    flag = models.IntegerField(null=True, db_column='FLAG', blank=True) # Field name made lowercase.
    aon_n = models.CharField(max_length=96, db_column='AON_N', blank=True) # Field name made lowercase.
    rate_plan = models.IntegerField(null=True, db_column='RATE_PLAN', blank=True) # Field name made lowercase.
    dnis = models.CharField(max_length=90, db_column='DNIS', blank=True) # Field name made lowercase.
    surch_plan = models.IntegerField(null=True, db_column='SURCH_PLAN', blank=True) # Field name made lowercase.
    bong = models.CharField(max_length=765, db_column='BONG', blank=True) # Field name made lowercase.
    periodic = models.CharField(max_length=765, db_column='PERIODIC', blank=True) # Field name made lowercase.
    tm = models.DateTimeField(db_column='TM') # Field name made lowercase.
    dest = models.CharField(max_length=60, db_column='DEST', blank=True) # Field name made lowercase.
    pin = models.CharField(max_length=60, db_column='PIN', blank=True) # Field name made lowercase.
    aon = models.CharField(max_length=60, db_column='AON', blank=True) # Field name made lowercase.
    alive_time = models.IntegerField(null=True, db_column='ALIVE_TIME', blank=True) # Field name made lowercase.
    unpaid = models.IntegerField(null=True, db_column='UNPAID', blank=True) # Field name made lowercase.
    conn_time = models.DateTimeField(null=True, db_column='CONN_TIME', blank=True) # Field name made lowercase.
    nas_ip = models.CharField(max_length=45, db_column='NAS_IP', blank=True) # Field name made lowercase.
    credit_time = models.IntegerField(null=True, db_column='CREDIT_TIME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SESS_PARAM'

class Site(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    sitename = models.CharField(max_length=60, db_column='SITENAME', blank=True) # Field name made lowercase.
    rate_t = models.IntegerField(null=True, blank=True)
    rate_o = models.IntegerField(null=True, blank=True)
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    roum_rate_s = models.IntegerField(null=True, blank=True)
    roum_rate_b = models.IntegerField(null=True, blank=True)
    client_rate = models.IntegerField(null=True, blank=True)
    rate_inet = models.IntegerField(null=True, blank=True)
    rate_inet_o = models.IntegerField(null=True, blank=True)
    rate_inet_t = models.IntegerField(null=True, blank=True)
    hunt_mode = models.IntegerField(null=True, blank=True)
    disc_rate_o = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    disc_rate_t = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    disc_roum_rate_s = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    disc_roum_rate_b = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    disc_client_rate = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    disc_inet_t = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    disc_inet_o = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    serve_rate_o = models.IntegerField(null=True, blank=True)
    serve_roum_rate_s = models.IntegerField(null=True, blank=True)
    serve_inet_t = models.IntegerField(null=True, blank=True)
    serve_inet_o = models.IntegerField(null=True, blank=True)
    serve_client_rate = models.IntegerField(null=True, blank=True)
    serve_rate_t = models.IntegerField(null=True, blank=True)
    serve_roum_rate_b = models.IntegerField(null=True, blank=True)
    rgrp_id_o = models.IntegerField(null=True, db_column='RGRP_ID_O', blank=True) # Field name made lowercase.
    rgrp_deny_id_o = models.IntegerField(null=True, db_column='RGRP_DENY_ID_O', blank=True) # Field name made lowercase.
    rgrp_id_t = models.IntegerField(null=True, db_column='RGRP_ID_T', blank=True) # Field name made lowercase.
    rgrp_deny_id_t = models.IntegerField(null=True, db_column='RGRP_DENY_ID_T', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SITE'

class SiteRateHistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    site_id = models.IntegerField(db_column='SITE_ID') # Field name made lowercase.
    act_date = models.DateField(null=True, db_column='ACT_DATE', blank=True) # Field name made lowercase.
    new_rate = models.IntegerField(null=True, db_column='NEW_RATE', blank=True) # Field name made lowercase.
    rate_type = models.IntegerField(null=True, db_column='RATE_TYPE', blank=True) # Field name made lowercase.
    old_rate = models.IntegerField(null=True, db_column='OLD_RATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SITE_RATE_HISTORY'

class SiteRateType(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=450, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'SITE_RATE_TYPE'

class SiteTemp(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    opername = models.CharField(max_length=300, db_column='OPERNAME', blank=True) # Field name made lowercase.
    descr = models.CharField(max_length=765, blank=True)
    agent_id = models.IntegerField(null=True, blank=True)
    agent_proc_o = models.IntegerField(null=True, blank=True)
    agent_proc_t = models.IntegerField(null=True, blank=True)
    rate_t = models.IntegerField(null=True, blank=True)
    rate_o = models.IntegerField(null=True, blank=True)
    manager_id = models.IntegerField(null=True, blank=True)
    orgname = models.CharField(max_length=150, db_column='ORGNAME', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=150, db_column='ADDRESS', blank=True) # Field name made lowercase.
    tels = models.CharField(max_length=300, db_column='TELS', blank=True) # Field name made lowercase.
    fin_person = models.CharField(max_length=60, db_column='FIN_PERSON', blank=True) # Field name made lowercase.
    fin_mail = models.CharField(max_length=150, db_column='FIN_MAIL', blank=True) # Field name made lowercase.
    tech_person = models.CharField(max_length=60, db_column='TECH_PERSON', blank=True) # Field name made lowercase.
    tech_mail = models.CharField(max_length=150, db_column='TECH_MAIL', blank=True) # Field name made lowercase.
    auto_inv = models.IntegerField(null=True, blank=True)
    mail_inv = models.IntegerField(null=True, blank=True)
    mail_det = models.IntegerField(null=True, blank=True)
    period_inv = models.IntegerField(null=True, blank=True)
    balance = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    pay_type = models.IntegerField(null=True, blank=True)
    max_credit = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    prihod = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rashod = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    acd = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ACD', blank=True) # Field name made lowercase.
    asr = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ASR', blank=True) # Field name made lowercase.
    shcalls = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SHCALLS', blank=True) # Field name made lowercase.
    allmin = models.IntegerField(null=True, db_column='ALLMIN', blank=True) # Field name made lowercase.
    allcalls = models.IntegerField(null=True, db_column='ALLCALLS', blank=True) # Field name made lowercase.
    shcnt = models.IntegerField(null=True, db_column='SHCNT', blank=True) # Field name made lowercase.
    success = models.IntegerField(null=True, db_column='SUCCESS', blank=True) # Field name made lowercase.
    sort_type = models.IntegerField(null=True, blank=True)
    min_proc = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    oper_state = models.IntegerField(null=True, blank=True)
    oper_id = models.IntegerField(null=True, db_column='OPER_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SITE_TEMP'

class SrcNumTranslate(models.Model):
    src_num = models.CharField(unique=True, max_length=60, db_column='SRC_NUM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SRC_NUM_TRANSLATE'

class Surcharges(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    surch_id = models.IntegerField(unique=True, null=True, db_column='SURCH_ID', blank=True) # Field name made lowercase.
    area_id = models.IntegerField(unique=True, null=True, db_column='AREA_ID', blank=True) # Field name made lowercase.
    area_type = models.IntegerField(unique=True, null=True, db_column='AREA_TYPE', blank=True) # Field name made lowercase.
    s_type = models.IntegerField(unique=True, null=True, db_column='S_TYPE', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    tm = models.IntegerField(null=True, db_column='TM', blank=True) # Field name made lowercase.
    start_date = models.DateField(unique=True, null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    state = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'SURCHARGES'

class SurchargeNames(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='NAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SURCHARGE_NAMES'

class SvodSend(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user = models.CharField(max_length=90, primary_key=True)
    status = models.IntegerField(null=True, blank=True)
    mail_to = models.CharField(max_length=150, blank=True)
    oper_id = models.IntegerField(null=True, blank=True)
    host = models.CharField(max_length=60, blank=True)
    term_orig = models.IntegerField(null=True, blank=True)
    dest_code = models.CharField(max_length=30, blank=True)
    sel_agent = models.IntegerField(null=True, blank=True)
    stat_type = models.IntegerField(null=True, blank=True)
    dest_group = models.IntegerField(null=True, blank=True)
    per_type = models.IntegerField(null=True, blank=True)
    add_days = models.IntegerField(null=True, blank=True)
    days_cnt = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'SVOD_SEND'

class SysEvents(models.Model):
    table_name = models.CharField(unique=True, max_length=60, db_column='TABLE_NAME') # Field name made lowercase.
    radius_port = models.IntegerField(unique=True, null=True, db_column='RADIUS_PORT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'SYS_EVENTS'

class Sendfile(models.Model):
    mailid = models.IntegerField(null=True, db_column='MailID', blank=True) # Field name made lowercase.
    filename = models.CharField(max_length=765, db_column='Filename', blank=True) # Field name made lowercase.
    file = models.TextField(blank=True)
    class Meta:
        db_table = u'SendFile'

class TempFiles(models.Model):
    fname = models.CharField(max_length=300, db_column='FNAME', blank=True) # Field name made lowercase.
    ctime = models.DateTimeField(db_column='CTIME') # Field name made lowercase.
    class Meta:
        db_table = u'TEMP_FILES'

class TerinalsIp(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    terminal_ip = models.CharField(max_length=54, db_column='TERMINAL_IP') # Field name made lowercase.
    ip_addr = models.BigIntegerField(db_column='IP_ADDR') # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME') # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME') # Field name made lowercase.
    class Meta:
        db_table = u'TERINALS_IP'

class Terminals(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    number = models.CharField(unique=True, max_length=96, db_column='NUMBER', blank=True) # Field name made lowercase.
    pin = models.CharField(max_length=96, db_column='PIN', blank=True) # Field name made lowercase.
    pin_key = models.CharField(max_length=30, db_column='PIN_KEY', blank=True) # Field name made lowercase.
    type = models.IntegerField(null=True, db_column='TYPE', blank=True) # Field name made lowercase.
    category = models.IntegerField(null=True, db_column='CATEGORY', blank=True) # Field name made lowercase.
    site_id = models.IntegerField(unique=True, null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    min_amount = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='MIN_AMOUNT', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='STATUS', blank=True) # Field name made lowercase.
    max_seans = models.IntegerField(null=True, db_column='MAX_SEANS', blank=True) # Field name made lowercase.
    date_active = models.DateTimeField(null=True, db_column='DATE_ACTIVE', blank=True) # Field name made lowercase.
    date_close = models.DateTimeField(null=True, db_column='DATE_CLOSE', blank=True) # Field name made lowercase.
    last_use = models.DateTimeField(null=True, db_column='LAST_USE', blank=True) # Field name made lowercase.
    last_active = models.DateTimeField(null=True, db_column='LAST_ACTIVE', blank=True) # Field name made lowercase.
    prepaid = models.IntegerField(null=True, db_column='PREPAID', blank=True) # Field name made lowercase.
    aon_mode = models.IntegerField(null=True, db_column='AON_MODE', blank=True) # Field name made lowercase.
    card_num = models.IntegerField(unique=True, null=True, db_column='CARD_NUM', blank=True) # Field name made lowercase.
    service = models.IntegerField(null=True, db_column='SERVICE', blank=True) # Field name made lowercase.
    lang = models.CharField(max_length=9, db_column='LANG', blank=True) # Field name made lowercase.
    pcard_id = models.IntegerField(null=True, db_column='PCARD_ID', blank=True) # Field name made lowercase.
    nominal = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='NOMINAL', blank=True) # Field name made lowercase.
    free = models.CharField(max_length=3, db_column='FREE', blank=True) # Field name made lowercase.
    next_subpay_date = models.DateTimeField(null=True, db_column='NEXT_SUBPAY_DATE', blank=True) # Field name made lowercase.
    date_create = models.DateTimeField(null=True, db_column='DATE_CREATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TERMINALS'

class TerminalsIp(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    terminal_ip = models.CharField(max_length=54, db_column='TERMINAL_IP') # Field name made lowercase.
    ip_addr = models.BigIntegerField(db_column='IP_ADDR') # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME') # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME') # Field name made lowercase.
    class Meta:
        db_table = u'TERMINALS_IP'

class TermAccess(models.Model):
    term_id = models.IntegerField(null=True, db_column='TERM_ID', blank=True) # Field name made lowercase.
    number = models.CharField(max_length=96, db_column='NUMBER', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TERM_ACCESS'

class Timezone(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(unique=True, max_length=90, db_column='NAME', blank=True) # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True) # Field name made lowercase.
    day0 = models.IntegerField(null=True, db_column='DAY0', blank=True) # Field name made lowercase.
    day1 = models.IntegerField(null=True, db_column='DAY1', blank=True) # Field name made lowercase.
    day2 = models.IntegerField(null=True, db_column='DAY2', blank=True) # Field name made lowercase.
    day3 = models.IntegerField(null=True, db_column='DAY3', blank=True) # Field name made lowercase.
    day4 = models.IntegerField(null=True, db_column='DAY4', blank=True) # Field name made lowercase.
    day5 = models.IntegerField(null=True, db_column='DAY5', blank=True) # Field name made lowercase.
    day6 = models.IntegerField(null=True, db_column='DAY6', blank=True) # Field name made lowercase.
    allow_tz = models.IntegerField(null=True, db_column='ALLOW_TZ', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TIMEZONE'

class TimePeriod(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    time1 = models.TextField(unique=True, db_column='TIME1', blank=True) # Field name made lowercase. This field type is a guess.
    time2 = models.TextField(unique=True, db_column='TIME2', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'TIME_PERIOD'

class TmpCdr(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_in = models.CharField(max_length=60, db_column='SRC_NUMBER_IN', blank=True) # Field name made lowercase.
    src_number_out = models.CharField(max_length=60, db_column='SRC_NUMBER_OUT', blank=True) # Field name made lowercase.
    dst_number_in = models.CharField(max_length=60, db_column='DST_NUMBER_IN', blank=True) # Field name made lowercase.
    dst_number_out = models.CharField(max_length=60, db_column='DST_NUMBER_OUT', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    src_port = models.IntegerField(null=True, db_column='SRC_PORT', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    dst_port = models.IntegerField(null=True, db_column='DST_PORT', blank=True) # Field name made lowercase.
    src_user = models.CharField(max_length=45, db_column='SRC_USER', blank=True) # Field name made lowercase.
    dst_user = models.CharField(max_length=45, db_column='DST_USER', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    connect_time = models.DateTimeField(null=True, db_column='CONNECT_TIME', blank=True) # Field name made lowercase.
    disconnect_time = models.DateTimeField(null=True, db_column='DISCONNECT_TIME', blank=True) # Field name made lowercase.
    elapsed_time = models.IntegerField(null=True, db_column='ELAPSED_TIME', blank=True) # Field name made lowercase.
    disconnect_code_local = models.IntegerField(null=True, db_column='DISCONNECT_CODE_LOCAL', blank=True) # Field name made lowercase.
    disconnect_code_q931 = models.IntegerField(null=True, db_column='DISCONNECT_CODE_Q931', blank=True) # Field name made lowercase.
    src_bytes_in = models.IntegerField(null=True, db_column='SRC_BYTES_IN', blank=True) # Field name made lowercase.
    src_bytes_out = models.IntegerField(null=True, db_column='SRC_BYTES_OUT', blank=True) # Field name made lowercase.
    dst_bytes_in = models.IntegerField(null=True, db_column='DST_BYTES_IN', blank=True) # Field name made lowercase.
    dst_bytes_out = models.IntegerField(null=True, db_column='DST_BYTES_OUT', blank=True) # Field name made lowercase.
    src_codec = models.CharField(max_length=765, db_column='SRC_CODEC', blank=True) # Field name made lowercase.
    dst_codec = models.CharField(max_length=765, db_column='DST_CODEC', blank=True) # Field name made lowercase.
    proxy_mode = models.IntegerField(null=True, db_column='PROXY_MODE', blank=True) # Field name made lowercase.
    route_retries = models.IntegerField(null=True, db_column='ROUTE_RETRIES', blank=True) # Field name made lowercase.
    qos = models.IntegerField(null=True, db_column='QOS', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    lar_fault_reason = models.IntegerField(null=True, db_column='LAR_FAULT_REASON', blank=True) # Field name made lowercase.
    bill_date = models.DateField(null=True, db_column='BILL_DATE', blank=True) # Field name made lowercase.
    remote_gatekeeper_ip = models.CharField(max_length=45, db_column='REMOTE_GATEKEEPER_IP', blank=True) # Field name made lowercase.
    bill_time = models.TextField(db_column='BILL_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    price_orig = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    rate_t = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rate_o = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    cid = models.IntegerField(db_column='CID') # Field name made lowercase.
    class Meta:
        db_table = u'TMP_CDR'

class TmpRadonline(models.Model):
    host = models.CharField(max_length=60, db_column='HOST', blank=True) # Field name made lowercase.
    src_number_bill = models.CharField(max_length=60, db_column='SRC_NUMBER_BILL', blank=True) # Field name made lowercase.
    dst_number_bill = models.CharField(max_length=60, db_column='DST_NUMBER_BILL', blank=True) # Field name made lowercase.
    src_ip = models.CharField(max_length=60, db_column='SRC_IP', blank=True) # Field name made lowercase.
    dst_ip = models.CharField(max_length=60, db_column='DST_IP', blank=True) # Field name made lowercase.
    callid = models.CharField(max_length=120, db_column='CALLID', blank=True) # Field name made lowercase.
    confid = models.CharField(max_length=120, db_column='CONFID', blank=True) # Field name made lowercase.
    setup_time = models.DateTimeField(null=True, db_column='SETUP_TIME', blank=True) # Field name made lowercase.
    acct_id = models.CharField(max_length=90, db_column='ACCT_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TMP_RADONLINE'

class Wifionline(models.Model):
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    start_time = models.TextField(db_column='START_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    nasport = models.CharField(max_length=90, db_column='NASPORT', blank=True) # Field name made lowercase.
    nasip = models.CharField(max_length=45, db_column='NASIP', blank=True) # Field name made lowercase.
    nasid = models.CharField(max_length=90, db_column='NASID', blank=True) # Field name made lowercase.
    uid = models.IntegerField(null=True, db_column='UID', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=150, db_column='USERNAME', blank=True) # Field name made lowercase.
    rate_plan = models.IntegerField(null=True, db_column='RATE_PLAN', blank=True) # Field name made lowercase.
    framedip = models.CharField(max_length=45, db_column='FRAMEDIP', blank=True) # Field name made lowercase.
    octets_in = models.IntegerField(null=True, db_column='OCTETS_IN', blank=True) # Field name made lowercase.
    octets_out = models.IntegerField(null=True, db_column='OCTETS_OUT', blank=True) # Field name made lowercase.
    session_time = models.IntegerField(null=True, db_column='SESSION_TIME', blank=True) # Field name made lowercase.
    ani = models.CharField(max_length=75, db_column='ANI', blank=True) # Field name made lowercase.
    alive_tm = models.DateTimeField(db_column='ALIVE_TM') # Field name made lowercase.
    dnis = models.CharField(max_length=75, db_column='DNIS', blank=True) # Field name made lowercase.
    acct_sess_id = models.CharField(max_length=51, primary_key=True, db_column='ACCT_SESS_ID') # Field name made lowercase.
    class Meta:
        db_table = u'WIFIONLINE'

class WifiAccounting(models.Model):
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    start_time = models.TextField(db_column='START_TIME', blank=True) # Field name made lowercase. This field type is a guess.
    nasport = models.CharField(max_length=90, db_column='NASPORT', blank=True) # Field name made lowercase.
    nasip = models.CharField(max_length=45, db_column='NASIP', blank=True) # Field name made lowercase.
    nasid = models.CharField(max_length=90, db_column='NASID', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=150, db_column='USERNAME', blank=True) # Field name made lowercase.
    octets_in = models.IntegerField(null=True, db_column='OCTETS_IN', blank=True) # Field name made lowercase.
    octets_out = models.IntegerField(null=True, db_column='OCTETS_OUT', blank=True) # Field name made lowercase.
    framedip = models.CharField(max_length=45, db_column='FRAMEDIP', blank=True) # Field name made lowercase.
    session_time = models.IntegerField(null=True, db_column='SESSION_TIME', blank=True) # Field name made lowercase.
    rate = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='RATE', blank=True) # Field name made lowercase.
    amount = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    term_id = models.IntegerField(null=True, db_column='TERM_ID', blank=True) # Field name made lowercase.
    result = models.IntegerField(null=True, db_column='RESULT', blank=True) # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    ani = models.CharField(max_length=75, db_column='ANI', blank=True) # Field name made lowercase.
    dnis = models.CharField(max_length=75, db_column='DNIS', blank=True) # Field name made lowercase.
    acct_sess_id = models.CharField(max_length=51, db_column='ACCT_SESS_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'WIFI_ACCOUNTING'

class Basedict(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    phrase = models.TextField(blank=True)
    class Meta:
        db_table = u'basedict'

class Codes(models.Model):
    code = models.CharField(unique=True, max_length=60, blank=True)
    name = models.CharField(max_length=300, blank=True)
    code_id = models.IntegerField(primary_key=True)
    type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'codes'

class CommFiles(models.Model):
    comm_id = models.IntegerField()
    filename = models.CharField(max_length=90, blank=True)
    filepath = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'comm_files'

class Comments(models.Model):
    comm_id = models.IntegerField(primary_key=True)
    oper_id = models.IntegerField(null=True, blank=True)
    comm_date = models.DateTimeField()
    subj_id = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    user = models.CharField(max_length=90)
    class Meta:
        db_table = u'comments'

class FormInfo(models.Model):
    form_id = models.IntegerField(primary_key=True)
    form_name = models.CharField(max_length=60, blank=True)
    form_descr = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'form_info'

class Gatekeepers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    address = models.CharField(unique=True, max_length=45, blank=True)
    port = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=60, blank=True)
    password = models.CharField(max_length=60, blank=True)
    security = models.IntegerField(null=True, blank=True)
    terminal = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    keepalive = models.IntegerField(null=True, blank=True)
    prefixes = models.CharField(max_length=765, blank=True)
    mera_id = models.IntegerField(unique=True, null=True, blank=True)
    oper_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'gatekeepers'

class GroupInfo(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(unique=True, max_length=60, blank=True)
    group_descr = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'group_info'

class InfiParams(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField(null=True, blank=True)
    params = models.TextField(blank=True)
    group_lot_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'infi_params'

class Lang(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    lang = models.CharField(unique=True, max_length=60, blank=True)
    class Meta:
        db_table = u'lang'

class LastCall(models.Model):
    call_time = models.DateTimeField(null=True, blank=True)
    last_null = models.DateTimeField(null=True, blank=True)
    last_upd = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'last_call'

class LotRights(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    lot_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    show_key = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'lot_rights'

class MeraGates(models.Model):
    gate_id = models.IntegerField(unique=True, null=True, db_column='GATE_ID', blank=True) # Field name made lowercase.
    mera_id = models.IntegerField(unique=True, null=True, db_column='MERA_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mera_gates'

class Multiling(models.Model):
    langid = models.IntegerField(unique=True, null=True, db_column='langID', blank=True) # Field name made lowercase.
    phraseid = models.IntegerField(unique=True, null=True, db_column='phraseID', blank=True) # Field name made lowercase.
    phrase = models.TextField(blank=True)
    class Meta:
        db_table = u'multiling'

class OperIp(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    op_id = models.IntegerField(null=True, db_column='OP_ID', blank=True) # Field name made lowercase.
    ip_op = models.CharField(max_length=60, db_column='IP_OP', blank=True) # Field name made lowercase.
    gateway_id = models.CharField(max_length=150, db_column='GATEWAY_ID', blank=True) # Field name made lowercase.
    route = models.IntegerField(null=True, blank=True)
    proxy_type = models.IntegerField(null=True, blank=True)
    gateway_mode = models.IntegerField(null=True, blank=True)
    gateway_type = models.IntegerField(null=True, blank=True)
    ip_precedence = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    mera_id = models.IntegerField(null=True, db_column='MERA_ID', blank=True) # Field name made lowercase.
    dst_translate = models.CharField(max_length=765, blank=True)
    in_dst_translate = models.CharField(max_length=765, blank=True)
    src_translate = models.CharField(max_length=765, blank=True)
    gatekeeper = models.CharField(max_length=90, blank=True)
    port = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=60, blank=True)
    password = models.CharField(max_length=60, blank=True)
    security = models.IntegerField(null=True, blank=True)
    terminal = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    keepalive = models.IntegerField(null=True, blank=True)
    prefixes = models.CharField(max_length=765, blank=True)
    rec_type = models.IntegerField(null=True, blank=True)
    mask = models.CharField(max_length=45, db_column='MASK', blank=True) # Field name made lowercase.
    gateway_port = models.IntegerField(null=True, blank=True)
    nat_rtp = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    state = models.IntegerField(null=True, blank=True)
    addparam = models.TextField(blank=True)
    stop_date = models.DateField(null=True, db_column='STOP_DATE', blank=True) # Field name made lowercase.
    start_date = models.DateField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    number = models.CharField(max_length=150, blank=True)
    net_addr = models.IntegerField(null=True, db_column='NET_ADDR', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'oper_ip'

class OperRights(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    oper_id = models.IntegerField(unique=True, null=True, blank=True)
    user_id = models.IntegerField(unique=True, null=True, blank=True)
    r_term = models.IntegerField(null=True, blank=True)
    r_orig = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'oper_rights'

class Operators(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    opername = models.CharField(max_length=300, db_column='OPERNAME', blank=True) # Field name made lowercase.
    descr = models.CharField(max_length=765, blank=True)
    agent_id = models.IntegerField(null=True, blank=True)
    agent_proc_o = models.IntegerField(null=True, blank=True)
    agent_proc_t = models.IntegerField(null=True, blank=True)
    rate_t = models.IntegerField(null=True, blank=True)
    rate_o = models.IntegerField(null=True, blank=True)
    manager_id = models.IntegerField(null=True, blank=True)
    orgname = models.TextField(db_column='ORGNAME', blank=True) # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True) # Field name made lowercase.
    tels = models.TextField(db_column='TELS', blank=True) # Field name made lowercase.
    fin_person = models.CharField(max_length=165, db_column='FIN_PERSON', blank=True) # Field name made lowercase.
    fin_mail = models.CharField(max_length=765, db_column='FIN_MAIL', blank=True) # Field name made lowercase.
    tech_person = models.CharField(max_length=165, db_column='TECH_PERSON', blank=True) # Field name made lowercase.
    tech_mail = models.CharField(max_length=765, db_column='TECH_MAIL', blank=True) # Field name made lowercase.
    auto_inv = models.IntegerField(null=True, blank=True)
    mail_inv = models.IntegerField(null=True, blank=True)
    mail_det = models.IntegerField(null=True, blank=True)
    period_inv = models.IntegerField(null=True, blank=True)
    balance = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    pay_type = models.IntegerField(null=True, blank=True)
    max_credit = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    prihod = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    rashod = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    acd = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ACD', blank=True) # Field name made lowercase.
    asr = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='ASR', blank=True) # Field name made lowercase.
    shcalls = models.DecimalField(decimal_places=4, null=True, max_digits=14, db_column='SHCALLS', blank=True) # Field name made lowercase.
    allmin = models.IntegerField(null=True, db_column='ALLMIN', blank=True) # Field name made lowercase.
    allcalls = models.IntegerField(null=True, db_column='ALLCALLS', blank=True) # Field name made lowercase.
    shcnt = models.IntegerField(null=True, db_column='SHCNT', blank=True) # Field name made lowercase.
    success = models.IntegerField(null=True, db_column='SUCCESS', blank=True) # Field name made lowercase.
    sort_type = models.IntegerField(null=True, blank=True)
    min_proc = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    oper_state = models.IntegerField(null=True, blank=True)
    time_diff = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    q931code = models.IntegerField(null=True, db_column='Q931code', blank=True) # Field name made lowercase.
    tech_icq = models.IntegerField(null=True, db_column='TECH_ICQ', blank=True) # Field name made lowercase.
    fin_icq = models.IntegerField(null=True, db_column='FIN_ICQ', blank=True) # Field name made lowercase.
    fax = models.TextField(db_column='FAX', blank=True) # Field name made lowercase.
    comp_id = models.IntegerField(null=True, blank=True)
    oper_type = models.IntegerField(null=True, blank=True)
    inv_mail = models.CharField(max_length=765, db_column='INV_MAIL', blank=True) # Field name made lowercase.
    wmz = models.CharField(max_length=60, db_column='WMZ', blank=True) # Field name made lowercase.
    currency = models.CharField(max_length=9, db_column='CURRENCY', blank=True) # Field name made lowercase.
    contract = models.CharField(max_length=150, blank=True)
    tz = models.CharField(max_length=90, db_column='TZ', blank=True) # Field name made lowercase.
    tz_route = models.CharField(max_length=3, db_column='TZ_ROUTE', blank=True) # Field name made lowercase.
    fin_msn = models.CharField(max_length=765, db_column='FIN_MSN', blank=True) # Field name made lowercase.
    tech_msn = models.CharField(max_length=765, db_column='TECH_MSN', blank=True) # Field name made lowercase.
    make_doc = models.IntegerField(null=True, blank=True)
    rate_mail = models.CharField(max_length=765, db_column='RATE_MAIL', blank=True) # Field name made lowercase.
    rate_increment_days = models.IntegerField(null=True, db_column='RATE_INCREMENT_DAYS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'operators'

class Options(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    form = models.CharField(max_length=60)
    param = models.CharField(max_length=90)
    value = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=90)
    class Meta:
        db_table = u'options'

class RateRights(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rate_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    r_view = models.IntegerField(null=True, blank=True)
    r_edit = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rate_rights'

class RetailPay(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    client_id = models.IntegerField(null=True, blank=True)
    pay_date = models.DateTimeField()
    pay_summ = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    user = models.CharField(max_length=60, blank=True)
    pay_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'retail_pay'

class RightsInfo(models.Model):
    rights_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(unique=True, null=True, blank=True)
    form_id = models.IntegerField(unique=True, null=True, blank=True)
    r_view = models.CharField(max_length=9, blank=True)
    r_edit = models.CharField(max_length=9, blank=True)
    r_adv = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'rights_info'

class RouteParam(models.Model):
    direction = models.IntegerField(unique=True, null=True, blank=True)
    oper_id = models.IntegerField(unique=True, null=True, blank=True)
    dest_id = models.IntegerField(unique=True, null=True, blank=True)
    route_oper = models.IntegerField(null=True, blank=True)
    min_proc = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    enable = models.IntegerField(null=True, blank=True)
    sort_type = models.IntegerField(null=True, blank=True)
    first_route = models.IntegerField(null=True, blank=True)
    second_route = models.IntegerField(null=True, blank=True)
    third_route = models.IntegerField(null=True, blank=True)
    deny_routes = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'route_param'

class Rparam(models.Model):
    direction = models.IntegerField(unique=True, null=True, blank=True)
    oper_id = models.IntegerField(unique=True, null=True, blank=True)
    dest_id = models.IntegerField(unique=True, null=True, blank=True)
    route_oper = models.IntegerField(null=True, blank=True)
    min_proc = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    enable = models.IntegerField(null=True, blank=True)
    sort_type = models.IntegerField(null=True, blank=True)
    first_route = models.IntegerField(null=True, blank=True)
    second_route = models.IntegerField(null=True, blank=True)
    third_route = models.IntegerField(null=True, blank=True)
    deny_routes = models.CharField(max_length=765, blank=True)
    breakout = models.IntegerField(null=True, blank=True)
    code = models.CharField(unique=True, max_length=60, blank=True)
    state = models.IntegerField(null=True, blank=True)
    proper_reject = models.IntegerField(null=True, blank=True)
    term_capaciti = models.IntegerField(null=True, blank=True)
    grant_capacity = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    use_oper_percent = models.IntegerField(null=True, blank=True)
    use_oper_sort = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=60, blank=True)
    rp_date = models.DateTimeField()
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    smart_enable = models.IntegerField(null=True, blank=True)
    smart_proc = models.IntegerField(null=True, blank=True)
    smart_oper = models.IntegerField(null=True, blank=True)
    only_manual = models.IntegerField(null=True, blank=True)
    mera_id = models.IntegerField(unique=True, null=True, blank=True)
    call_side = models.IntegerField(null=True, blank=True)
    end_side_dest = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rparam'

class RparamBackup(models.Model):
    direction = models.IntegerField(null=True, blank=True)
    oper_id = models.IntegerField(null=True, blank=True)
    dest_id = models.IntegerField(null=True, blank=True)
    route_oper = models.IntegerField(null=True, blank=True)
    min_proc = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    enable = models.IntegerField(null=True, blank=True)
    sort_type = models.IntegerField(null=True, blank=True)
    first_route = models.IntegerField(null=True, blank=True)
    second_route = models.IntegerField(null=True, blank=True)
    third_route = models.IntegerField(null=True, blank=True)
    deny_routes = models.CharField(max_length=765, blank=True)
    breakout = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=60, blank=True)
    proper_reject = models.IntegerField(null=True, blank=True)
    term_capaciti = models.IntegerField(null=True, blank=True)
    grant_capacity = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    use_oper_percent = models.IntegerField(null=True, blank=True)
    use_oper_sort = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=60, blank=True)
    rp_date = models.DateTimeField()
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    smart_enable = models.IntegerField(null=True, blank=True)
    smart_proc = models.IntegerField(null=True, blank=True)
    smart_oper = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rparam_backup'

class SipCdr(models.Model):
    id = models.IntegerField(null=True, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=765, blank=True)
    called_num = models.CharField(max_length=60, blank=True)
    dtime = models.DateTimeField(null=True, blank=True)
    elapsed_time = models.IntegerField(null=True, blank=True)
    uniqid = models.CharField(max_length=765, blank=True)
    userip = models.CharField(max_length=45, blank=True)
    destip = models.CharField(max_length=45, blank=True)
    result = models.IntegerField(null=True, db_column='RESULT', blank=True) # Field name made lowercase.
    tarif = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='TARIF', blank=True) # Field name made lowercase.
    price = models.DecimalField(decimal_places=4, null=True, max_digits=16, db_column='PRICE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sip_cdr'

class SipLot(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    rate_o = models.IntegerField(null=True, blank=True)
    descr = models.CharField(max_length=765, blank=True)
    status = models.IntegerField(null=True, blank=True)
    host = models.CharField(max_length=45, blank=True)
    serial_start = models.CharField(max_length=60, blank=True)
    user_count = models.IntegerField(null=True, blank=True)
    is_credit = models.IntegerField(null=True, blank=True)
    lot_prefix = models.CharField(max_length=33, blank=True)
    pub_visible = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sip_lot'

class SipLotAmount(models.Model):
    id = models.IntegerField(primary_key=True)
    lot_id = models.IntegerField(null=True, blank=True)
    start_period = models.DateTimeField(null=True, blank=True)
    end_period = models.DateTimeField(null=True, blank=True)
    calledtime = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    attempts = models.IntegerField(null=True, blank=True)
    calls_count = models.IntegerField(null=True, blank=True)
    closed_flag = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sip_lot_amount'

class SipLotHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField(null=True, blank=True)
    newlot = models.IntegerField(null=True, blank=True)
    fromtime = models.DateTimeField(null=True, blank=True)
    operator = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'sip_lot_history'

class SipPin(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    pin = models.CharField(max_length=150, blank=True)
    state = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sip_pin'

class SipPs(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    type = models.CharField(max_length=18)
    secret = models.CharField(max_length=60)
    auth = models.CharField(max_length=60)
    nat = models.CharField(max_length=9)
    host = models.CharField(max_length=90)
    canreinvite = models.CharField(max_length=9)
    qualify = models.CharField(max_length=30)
    callerid = models.CharField(max_length=240)
    disallaw = models.CharField(max_length=75)
    allow = models.CharField(max_length=240, blank=True)
    context = models.CharField(max_length=150, blank=True)
    mailbox = models.CharField(max_length=150)
    lot_id = models.IntegerField(null=True, blank=True)
    ast_id = models.IntegerField(null=True, db_column='AST_ID', blank=True) # Field name made lowercase.
    amount = models.DecimalField(null=True, max_digits=14, decimal_places=4, blank=True)
    confirm = models.IntegerField(null=True, blank=True)
    user_group = models.CharField(max_length=150, blank=True)
    login = models.CharField(max_length=150, blank=True)
    ext_type = models.IntegerField(null=True, blank=True)
    currency_id = models.IntegerField(null=True, blank=True)
    fio = models.CharField(max_length=765, blank=True)
    number = models.CharField(max_length=60, blank=True)
    is_credit = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sip_ps'

class SipSess(models.Model):
    id = models.IntegerField(null=True, blank=True)
    conf_id = models.CharField(max_length=765, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=765, blank=True)
    dst_num = models.CharField(max_length=60, blank=True)
    dest_id = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    connect_time = models.DateTimeField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    nas_ip = models.CharField(max_length=45, blank=True)
    price = models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)
    class Meta:
        db_table = u'sip_sess'

class SiteNfStat(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    site_id = models.IntegerField(null=True, db_column='SITE_ID', blank=True) # Field name made lowercase.
    net_id = models.IntegerField(null=True, db_column='NET_ID', blank=True) # Field name made lowercase.
    in_traf = models.BigIntegerField(null=True, db_column='IN_TRAF', blank=True) # Field name made lowercase.
    out_traf = models.BigIntegerField(null=True, db_column='OUT_TRAF', blank=True) # Field name made lowercase.
    start_date = models.DateTimeField(null=True, db_column='START_DATE', blank=True) # Field name made lowercase.
    end_date = models.DateTimeField(null=True, db_column='END_DATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'site_nf_stat'

class SmsLog(models.Model):
    id = models.IntegerField(primary_key=True)
    card_id = models.IntegerField()
    operator = models.CharField(max_length=750)
    phone_called = models.CharField(max_length=750)
    phone_calling = models.CharField(max_length=750)
    text = models.CharField(max_length=750)
    class Meta:
        db_table = u'sms_log'

class Templates(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.CharField(max_length=60, blank=True)
    file = models.TextField(blank=True)
    name = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'templates'

class Tmpdictokhoruzhenko(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'tmpDictokhoruzhenko'

class Tmplogsokhoruzhenko(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    logdate = models.CharField(max_length=19, db_column='LOGDATE', blank=True) # Field name made lowercase.
    form_id = models.IntegerField(null=True, db_column='FORM_ID', blank=True) # Field name made lowercase.
    action_id = models.IntegerField(null=True, db_column='ACTION_ID', blank=True) # Field name made lowercase.
    filename = models.CharField(max_length=300, db_column='FILENAME', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tmpLOGSokhoruzhenko'

class Tmppaysokhoruzhenko(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    pay_date = models.DateField(null=True, db_column='PAY_DATE', blank=True) # Field name made lowercase.
    db_date = models.DateField(null=True, db_column='DB_DATE', blank=True) # Field name made lowercase.
    pay_sum = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='PAY_SUM', blank=True) # Field name made lowercase.
    pay_fact = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='PAY_FACT', blank=True) # Field name made lowercase.
    pay_type = models.IntegerField(null=True, db_column='PAY_TYPE', blank=True) # Field name made lowercase.
    comment = models.CharField(max_length=765, db_column='COMMENT', blank=True) # Field name made lowercase.
    user = models.CharField(max_length=60, db_column='USER', blank=True) # Field name made lowercase.
    cur_name = models.CharField(max_length=15, db_column='CUR_NAME', blank=True) # Field name made lowercase.
    exch_rate = models.DecimalField(decimal_places=6, null=True, max_digits=14, db_column='EXCH_RATE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tmpPAYSokhoruzhenko'

class UserInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=90)
    user_passwd = models.CharField(max_length=300, blank=True)
    user_group = models.CharField(max_length=60, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    user_fio = models.CharField(max_length=90, blank=True)
    all_opers = models.IntegerField(null=True, blank=True)
    all_rates = models.IntegerField(null=True, blank=True)
    all_lots = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_info'

class Wmpays(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    url = models.CharField(max_length=765, blank=True)
    amount = models.DecimalField(null=True, max_digits=14, decimal_places=2, blank=True)
    data = models.DateTimeField(null=True, blank=True)
    guid = models.CharField(max_length=765, blank=True)
    confirm = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=60, blank=True)
    wmid_payer = models.CharField(max_length=45, blank=True)
    purse_payer = models.CharField(max_length=45, blank=True)
    sys_invs = models.IntegerField(null=True, blank=True)
    sys_trans = models.IntegerField(null=True, blank=True)
    wmdate = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'wmpays'

class Wmtrans(models.Model):
    id = models.IntegerField(primary_key=True)
    sourcetrn = models.IntegerField()
    wmtrn = models.IntegerField()
    op_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'wmtrans'


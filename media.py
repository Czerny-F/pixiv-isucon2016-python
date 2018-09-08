import MySQLdb.cursors

DIR = '/home/isucon/private_isu/webapp/media'
PATH = '/image/'

EXTS = {
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'image/gif': 'gif',
}

DBCONF = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'db': 'isuconp',
    'charset': 'utf8mb4',
    'cursorclass': MySQLdb.cursors.DictCursor,
    'autocommit': True,
}

db = MySQLdb.connect(**DBCONF)

csr = db.cursor()
csr.execute('SELECT id FROM posts')
# csr.execute('SELECT id, mime, imgdata FROM posts')

for post in csr.fetchall():
    pid = post['id']
    csr.execute('SELECT mime, imgdata FROM posts WHERE id = %s', (pid,))
    p = csr.fetchone()

    name = '%s.%s' % (pid, EXTS[p['mime']])
    fname = '%s/%s' % (DIR, name)
    url = '%s%s' % (PATH, name)
    with open(fname, 'wb') as f:
        f.write(p['imgdata'])
    print(fname)

    csr.execute('UPDATE posts SET image = %s WHERE id = %s', (url, pid))
    print(url)

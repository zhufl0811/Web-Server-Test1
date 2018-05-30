import pymysql
db=pymysql.connect('localhost','root','0811','test',use_unicode=True, charset="utf8")

def query(name_like,price_min,price_max,rank):
    cursor = db.cursor()
    if name_like:
        if rank:
            sql='select * from phone where name like \'%'+name_like+'%\' and rank>'+rank
        else:
            sql= 'select * from phone where name like \'%'+name_like+'%\''
    else:
        if rank:
            sql = 'select * from phone where rank>' + rank         
        else:
            sql = 'select * from phone'   
    cursor.execute(sql)
    data = list(cursor.fetchall())
    result=data.copy()
    cursor.close()
    if price_min:
        if price_max:
            for q in data:
                try:
                    price=int(q[2][1:])
                    if price>int(price_min) and price<int(price_max):
                        pass
                    else:
                        result.remove(q)
                except:
                    result.remove(q)
        else:
            for q in data:
                try:
                    price=int(q[2][1:])
                    if price>int(price_min):
                        pass
                    else:
                        result.remove(q)
                except:
                    result.remove(q)
    else:
        if price_max:
            for q in data:
                try:
                    price=int(q[2][1:])
                    if price<int(price_max):
                        pass
                    else:
                        result.remove(q)
                except:
                    result.remove(q)
        else:
            pass
    return result

def add(name,price,rank):
    if price[0]=='￥':
        pass
    else:
        price = '￥'+price
    if float(rank):
        if float(rank)>10:
            rank=9.9
        elif float(rank)<0:
            rank=0.0
    else:
        rank=0.0
    cursor1 = db.cursor()
    rank = str(float(rank))
    sql = 'INSERT INTO phone(name,price,rank) values'+' (\''+name+'\',\''+price+'\','+ rank+')'
    print(sql)
    cursor1.execute(sql)
    db.commit()
    cursor1.close()

def edit_query(name):
    sql = 'select * from phone where name=\''+name+'\''
    cursor2=db.cursor()
    cursor2.execute(sql)
    data = cursor2.fetchone()
    cursor2.close()
    return data

def edit(origin_name,name,price,rank):
    if price[0]=='￥':
        pass
    else:
        price = '￥'+price
    if float(rank):
        if float(rank)>10:
            rank=9.9
        elif float(rank)<0:
            rank=0.0
    else:
        rank=0.0
    cursor3=db.cursor()
    cursor3.execute('select * from phone where name=\''+origin_name+'\'')
    origin_id=cursor3.fetchone()[0]
    sql = 'UPDATE phone SET name=\''+name+'\','+'price=\''+str(price)+'\','+'rank='+rank+' where id='+str(origin_id)
    cursor3.execute(sql)
    db.commit()
    cursor3.close()

def delete(origin_name):
    cursor4=db.cursor()
    sql = 'DELETE FROM phone WHERE name=\''+origin_name+'\''
    cursor4.execute(sql)
    db.commit()
    cursor4.close()


if __name__ == '__main__':
    # s=edit_query('vivo X21（全网通）')
    # print(s[1])
    s=delete('小米99')


from com.eurekamw_mg.model import UserFile as uf, CategoryFile as cf
from com.eurekamw_mg.utils import CategoryUtils as cu

def test_get_json():
    user = uf.User('administrator', 'Admin', 'password')
    print(user.get_json())

def run_test_suite():
    test_get_json()

cat1 = cf.Category('attack',['assail','belabor','triM','test','ttt'])
cat2 = cf.Category('agree',['accede','assent'])

cats=[]
cats.append(cat1)
cats.append(cat2)
print(cats)
cu.add_categories(cats)

# update_category('agree','agree2')

cu.add_words_to_category('attack',['assail','belabor'])

# run_test_suite()
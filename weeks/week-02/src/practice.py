class Node():   #Node sınıfı ikili ağaçtaki tek bir sınıfı kabul edecek.
    def __init__(self,text,value):  #Sınıfın kurucu metodudur.İinit metodu sınıfta yeni bir nesne oluştuğunda otomatik çalışır.
        self.text=text    #text düğümün ismi(mehmet). value düğümün sayısal değeridir(78).
        self.value=value
        self.left=None       #başlangıçta sağda ve solda çocuk olmadığı için none atanır.binarytree sınıfı ile yeni çocuklar atanabilir.
        self.right=None

class BinaryTree():
    def __init__(self,text:str,value:int):  #init metodu çalıştığında verilen key ve value değerleri ile bir roof(kök) yapısı oluşur
        self.root=Node(text,value)    #sonradan eklenilen her düğüm(add_node)bu düğümün altına yerleşir.

    def add_node(self,text,value):
        new_node=Node(text,value)
        current_node = self.root   #current_node ağaç üzerinde dolaşırken o an üzerinde bulunduğun değeri tutar.
        while True:
            if value>current_node.value:   #yeni değer mevcut değerden büyükse sağa bakılır.
                if current_node.right is None:   #eğer mevcut düğümün sağ çocuğu yoksa buraya eklenir.
                    current_node.right = new_node   #artık ağaçta yerini buldu.
                    break
                else:    #sağ taraf dolusa çalışır.
                    current_node=current_node.right
            elif value<current_node.value:      #yeni değer mevcut değerden küçük mü
                if current_node.left is None:    #düğümün sol çocuğu yoksa buraya eklenir.
                    current_node.left = new_node     #sol taraf boş olduğu için yeni düğümü sol çocuğa atıyruz.
                break
            else:
                current_node = current_node.left
        else:
            print("Hata oluştu.Değer zaten mevcut.")
            return
        

    def delete_node(self, root, value):
        if root is None:
            return root

        # Arama kısmı
        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            # 1. Çocuk yoksa
            if root.left is None and root.right is None:
                return None

            # 2. Tek çocuk varsa
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # 3. İki çocuk varsa
            else:
                successor = self.find_min(root.right)
                root.value = successor.value
                root.right = self.delete_node(root.right, successor.value)

        return root
    
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_value(self,value):    #self sınıfın kendisi temsil eder.
        current_node = self.root    #aramaya ağacın kökünden başlıyoruz.
        while current_node is not Node:    #Düğüm boş olmadığı sürece aramaya devam eder.
            if current_node.value == value:  #aradığımız değer mevcut değere eşitse text değerini alırız.
                return current_node.text
            if value<current_node.value:    #aradığımız değer mevcut değerden küçükse sola gitmeliyiz
                if current_node.left is None:   #sol taraf boşsa aradığımız değer yoktur.
                    return "Hata:Değer yok."
                current_node = current_node.left    #sol çocuğa ilerle ve aramaya devam et.
            elif value>current_node.value:    #aradığımız değer mevcut düğümden büyükse sağ tarafa gitmeliyiz.
                if current_node.right is None:
                    return "Hata:Değer yok."    #sağ taraf boşsa aradığımız değer yoktur
                current_node = current_node.right 
    def size(self):
        return self._size(self.root)
        
    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)
    def height(self):
        return self._height(self.root)
    def _height(self, current_node):
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left),self._height(current_node.right))
    
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("   " * level + f"({node.text}, {node.value})")
        print_tree(node.left, level + 1)

if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet",32)
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Konya",42)

    print_tree(my_tree.root)
    print(my_tree.find_value(41))
    print(my_tree.find_value(82))
    print(my_tree.size())
    print(my_tree.height())
    print_tree(my_tree.root)

    my_tree.root=my_tree.delete_node(my_tree.root,9)
                                    

    print("silmeden sonra: ")
    print(my_tree.root)


def print_tree(node, level=0):
    if node is not None:
        # Önce sağ dalı yazdır
        print_tree(node.right, level + 1)
        # Sonra kendisini yazdır
        print("    " * level + f"({node.text}, {node.value})")
        # En son sol dalı yazdır
        print_tree(node.left, level + 1)

# Kullanım:
print_tree(my_tree.root)



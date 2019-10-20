#!/usr/bin/python
def print_details():
    print
    print "=================================Items Details================================"
    print "%-15s%-35s%-20s%-20s" % ("Item no", "Item description", "Current Bid", "No. of bids")
    for it, it_dtls in items_d.items():
        print "%-15s" % (it),
        print "%-35s%-20s%-20s" % (it_dtls[0], it_dtls[3], it_dtls[2])
    print "=============================================================================="

def auction():
    print_details()
    buyer_no = str(raw_input("Enter your buyer id: "))
    item_no = str(raw_input("Which item do you want to place bid for: "))
    bid = input("Enter bid value(higher than current bid)")

    for it, it_dtls in items_d.items():
        if item_no in it:
            if bid > it_dtls[3]: #if provided bid is higher than current bid for item
                it_dtls[3] = bid #update current bid value of item
                it_dtls[2] += 1 #increase no. of bids for that item
                buyers_d[buyer_no][item_no] = bid
            else:
                print
                print
                print "Please enter bid value greater than current value !!"
                print
    print_details()

print "************Auction***********"
print "Define items"
no_items = input("Enter no. of items to define: ")

fee = 0.0
items_sold = 0
zero_bids = 0
auct = True
no_buyers = 0
items_d = {} #items dictionary containing items
items_t = [] #a temporary array for storing info about an item
buyers_d = {} #buyers dictionary

for x in range(1,no_items+1):
    print
    print "Item" + str(x)
    desc = str(raw_input("Enter description: "))
    res_price = input("Enter reserve price: ")
    no_bids = 0
    current_bid = 0
    sold = False

    items_t.append(desc)
    items_t.append(res_price)
    items_t.append(no_bids)
    items_t.append(current_bid)
    items_t.append(sold)

    items_d['i'+str(x)] = items_t
    items_t = [] #empty the array

print
no_buyers = input("Enter number of buyers: ")
for i in range(1,no_buyers+1): #initialise buyers dictionary
    buyers_d['b'+str(i)] = {}
print "+++++++++++++++++++++++++++++++++"
print "Buyers id are as follows"
print sorted(buyers_d.keys())
print
print "Items id are as follows"
print sorted(items_d.keys())
print "+++++++++++++++++++++++++++++++++"

while auct:
    auction()
    print
    print buyers_d
    print
    c = str(raw_input("Continue Auction (y/n): "))
    if c == "n":
        auct = False

for it, it_dtls in items_d.items():
    if it_dtls[3] >= it_dtls[1]: #if final bid is higher than reserved price for that item
        it_dtls[4] = True #mark item as sold
        fee = fee + it_dtls[3] + float(it_dtls[3])/10
        items_sold += 1
    elif it_dtls[2] == 0: #if no. of bids equals zero for that item
        zero_bids += 1

print
print "========================Items sold====================="
print "%-15s%-35s-%15s" % ("Item no", "Final Bid", "Reserve Price")
for it, it_dtls in items_d.items():
    if it_dtls[4] == True:
        print "%-15s%-35s-%15s" % (it, it_dtls[3],it_dtls[1])
print "========================================================"
print "Total fees is ", fee
print "--------------------------------------------------------"

print
print "===================Items with zero bids================="
for it, it_dtls in items_d.items():
    if it_dtls[2] == 0: #if no of bids equals zero for that item
        print "%-15s%-35s-%15s" % ("Item no", "Final Bid", "Reserve Price")
        print "%-15s%-35s-%15s" % (it, it_dtls[3],it_dtls[1])
print "========================================================="

print
print "========Bids that did not reach reserve price============"
print "%-15s%-35s-%15s" % ("Item no", "Final Bid", "Reserve Price")
for it, it_dtls in items_d.items():
    if it_dtls[4] == False:
        print "%-15s%-35s-%15s" % (it, it_dtls[3],it_dtls[1])
print "========================================================="

print
print "Items with zero bids: ", zero_bids
print "No. of unsold items: ", no_items - items_sold

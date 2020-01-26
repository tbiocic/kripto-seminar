from bitcoinrpc.authproxy import AuthServiceProxy

def connection():
    rpc_connection = AuthServiceProxy("http://student:WYVyF5DTERJASAiIiYGg4UkRH@blockchain.oss.unist.hr:8332")

    getnetworkinfo = rpc_connection.getnetworkinfo()
    getblockchaininfo= rpc_connection.getblockchaininfo()
    getnettotals = rpc_connection.getnettotals()
    getwalletinfo = rpc_connection.getwalletinfo()
    
    print ("BLOCKCHAIN INFO")
    print ("Tip mreže: %s"%(getblockchaininfo["chain"]))
    print ("Verzija: %s"%(getnetworkinfo["subversion"]))
    print ("Broj blokova: %s"%(getblockchaininfo["blocks"]))
    print ("Veličina blockchaina na disku: %s"%((getblockchaininfo["size_on_disk"])))
    print ("Težina: %s"%(getblockchaininfo["difficulty"]))
    print ("Primljeno: %s"%(getnettotals["totalbytesrecv"]))
    print ("Poslano: %s"%(getnettotals["totalbytessent"]))
    
    print ("\nWALLET INFO")
    print ("Naziv novčanika: %s"%(getwalletinfo["walletname"]))
    print ("Verzija novčanika: %s"%(getwalletinfo["walletversion"]))
    print ("Stanje novčanika: %f"%(getwalletinfo["balance"]))
    print ("Stanje novčanika (nepotvrđeno): %f "%(getwalletinfo["unconfirmed_balance"]))
    print ("Broj transakcija: %s"%(getwalletinfo["txcount"]))
    
if __name__=="__main__":
    connection()
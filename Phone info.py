#! /usr/bin/python3
brands = {
    "SAMSUNG": {
        "S": {"CPU": "ARM Cortex-A8 Hummingbird", "GPU": "PowerVR SGX540", "RAM": "512MB"},
        "S2": {"CPU": "Samsung Exynos 4210", "GPU": "ARM Mali-400 MP4", "RAM": "1GB"},
        "S3": {"CPU": "Samsung Exynos 4412/Qualcomm Snapdragon S4 Plus", "GPU": "ARM Mali-400 MP4/ATI Adreno 225", "RAM": "1GB"},
        "S4": {"CPU": "Qualcomm Snapdragon 600", "GPU": "ATI Adreno 320", "RAM": "2GB"},
        "S5": {"CPU": "Qualcomm Snapdragon 801", "GPU": "ATI Adreno 330", "RAM": "2GB"},
        "S6": {"CPU": "Samsung Exynos 7420", "GPU": "ARM Mali-T760 MP8", "RAM": "3GB"},
        "S7": {"CPU": "Samsung Exynos 8890","GPU": "ARM Mali-T880 MP12", "RAM": "4GB"},
        "S8": {"CPU": "Samsung Exynos 8895/Qualcomm Snapdragon 835","GPU": "ARM Mali-G71 MP20/ATI Adreno 540", "RAM" : "4GB"},
        "S9": {"CPU": "Samsung Exynos 9810/Qualcomm Snapdragon 845", "GPU": "ARM Mali-G72 MP18/ATI Adreno 630", "RAM": "4GB"},
        "S10": {"CPU": "Samsung Exynos 9820/Qualcomm Snapdragon 855", "GPU": "ARM Mali-G76 MP12/ATI Adreno 640", "RAM": "6/8GB"},
        "S20": {"CPU": "Samsung Exynos 990/Qualcomm Snapdragon 865", "GPU": "ARM Mali-G77 MP11/ATI Adreno 650", "RAM": "8GB"},
        "S20 FE":{"CPU": "Samsung Exynos 990", "GPU": "ARM Mali-G77 MP11", "RAM": "6/8GB"},
        "S20 FE 5G": {"CPU": "Qualcomm Snapdragon 865", "GPU": "ATI Adreno 650", "RAM": "6/8GB"},
        "S21": {"CPU": "Samsung Exynos 2100/Qualcomm Snapdragon 888", "GPU": "ARM Mali-G78 MP14/ATI Adreno 660", "RAM": "8GB"},
        "S22": {"CPU": "Samsung Exynos 2200/Qualcomm Snapdragon 8 Gen 1", "GPU": "AMD Xclipse 920 (RDNA2)/ATI Adreno 730", "RAM": "8GB"},
        "S23": {"CPU": "Qualcomm Snapdragon 8 Gen 2 OC Edition", "GPU": "ATI Adreno 740", "RAM": "8GB"},
        "FOLD":{"CPU": "Qualcomm Snapdragon 855", "GPU": "ATI Adreno 640", "RAM": "12GB"},
        "Z-FOLD 2":{"CPU": "Qualcomm Snapdragon 865", "GPU": "ATI Adreno 650", "RAM": "12GB"},
        "Z-FOLD 3":{"CPU": "Qualcomm Snapdragon 888", "GPU": "ATI Adreno 660", "RAM": "12GB"},
        "Z-FOLD 4":{"CPU": "Qualcomm Snapdragon 8+ Gen 1", "GPU": "ATI Adreno 730", "RAM": "12GB"},
        "Z-FOLD 5":{"CPU": "Qualcomm Snapdragon 8 Gen 2 OC Edition", "GPU": "ATI Adreno 740", "RAM": "12GB"},
        "A01":{"CPU": "Qualcomm Snapdragon 439", "GPU": "ATI Adreno 505", "RAM": "2GB"},
        "A01 CORE":{"CPU": "Mediatek MT6739", "GPU": "PowerVR GE8100", "RAM": "1/2GB"},
        "A10":{"CPU": "Samsung Exynos 7784", "GPU": "ARM Mali-G71", "RAM": "2/4GB"},
        "A20":{"CPU": "Samsung Exynos 7784", "GPU": "ARM Mali-G71", "RAM": "3GB"},
        "A30":{"CPU": "Samsung Exynos 7904", "GPU": "ARM Mali-G71 MP2", "RAM": "3/4GB"},
        "A40":{"CPU": "Samsung Exynos 7904", "GPU": "ARM Mali-G71 MP2", "RAM": "4GB"},
        "A50":{"CPU": "Samsung Exynos 9610", "GPU": "ARM Mali-G72 MP3", "RAM": "4/6GB"},
        "A60":{"CPU": "Qualcomm Snapdragon 675", "GPU": "ATI Adreno 612", "RAM": "6GB"},
        "A70":{"CPU": "Qualcomm Snapdragon 675", "GPU": "ATI Adreno 612", "RAM": "6/8GB"},
        "A80":{"CPU": "Qualcomm Snapdragon 730", "GPU": "ATI Adreno 618", "RAM": "8GB"},
        "A90 5G":{"CPU": "Qualcomm Snapdragon 855", "GPU": "ATI Adreno 640", "RAM": "6/8GB"},
        "A02":{"CPU": "Mediatek MT6739W", "GPU": "PowerVR GE8100", "RAM":"2/4GB"},
        "A02S":{"CPU": "Qualcomm Snapdragon 450", "GPU": "ATI Adreno 506", "RAM": "1/4GB"},
        "A03":{"CPU": "Unisoc T606", "GPU": "ARM Mali-G57 MP1", "RAM": "3/4GB"},
        "A03S":{"CPU": "Mediatek Helio P35", "GPU": "PowerVR GE8320", "RAM": "2/4GB"}, 
        "A03 CORE":{"CPU": "Unisoc SC9863A", "GPU": "IMG8322", "RAM": "2GB"},
        "A11": {"CPU": "Qualcomm Snapdragon 450", "GPU": "ATI Adreno 506", "RAM": "6/4GB"},
        "A12": {"CPU": "Mediatek Helio P35", "GPU": "PowerVR GE8320", "RAM": "2/6GB"},
        "A13": {"CPU": "Samsung Exynos 850", "GPU": "ARM Mali-G52", "RAM": "3/6GB"},
        "A13 5G": {"CPU": "Mediatek Dimensity 700", "GPU": "ARM Mali-G57 MC2", "RAM": "4/6GB"},
        "A14": {"CPU": "Mediatek Helio G80", "GPU": "ARM Mali-G52 MC2", "RAM": "4/6GB"},
        "A14 5G": {"CPU": "Samsung Exynos 1330", "GPU": "ARM Mali-G68 MP2", "RAM": "4/8GB"},
        "A20S": {"CPU": "Qualcomm Snapdragon 450", "GPU": "ATI Adreno 506", "RAM": "2/4GB"},
        "A20E": {"CPU": "Samsung Exynos 7884", "GPU": "ARM Mali-G71 MP2", "RAM": "3GB"},
        "A21": {"CPU": "Mediatek Helio P35", "GPU": "PowerVR GE8320", "RAM": "3GB"},
        "A21S": {"CPU": "Samsung Exynos 850", "GPU": "ARM Mali-G52", "RAM": "2/6GB"},
        "A22": {"CPU": "Mediatek MT6769V", "GPU": "ARM Mali-G52 MC2", "RAM": "4/6GB"},
        "A22 5G": {"CPU": "Mediatek Dimensity 700", "GPU": "ARM Mali-G57 MC2", "RAM": "4/8GB"},
        "A23": {"CPU": "Qualcomm Snapdragon 680", "GPU": "ATI Adreno 610", "RAM": "4/8GB"},
        "A23 5G": {"CPU": "Qualcomm Snapdragon 695 5G", "GPU": "ATI Adreno 619", "RAM": "4/8GB"},
        "A24": {"CPU": "Mediatek Helio G99", "GPU": "ARM Mali-G57 MC2", "RAM": "4/8GB"},
    },
    "Apple": {
    },
    # ... other brands and models
    }

def get_phone_info(brand, model):
    if brand in brands and model in brands[brand]:
        phone_info = brands[brand][model]
        return f"Brand: {brand}\nModel: {model}\nCPU: {phone_info['CPU']}\nGPU: {phone_info['GPU']}\nRAM: {phone_info['RAM']}"
    else:
        return "Phone not found in the database."

selected_brand = input("Enter a brand: ").upper()
selected_model = input("Enter a phone model: ").upper()
info = get_phone_info(selected_brand, selected_model)
print(info)
input("Press a Button to Quit... ")

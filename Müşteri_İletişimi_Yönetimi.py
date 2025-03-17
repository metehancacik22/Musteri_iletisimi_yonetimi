import numpy as np


# Müşteri Destek Temsilcisi Yönlendirme - Dinamik Programlama Yaklaşımı
# Temsilciler ve müşteriler arasındaki atamayı optimize eden DP tabanlı bir algoritma

def optimize_agent_allocation(requests, agents):
    """
    Müşteri taleplerine göre temsilcileri yönlendirir.
    Dinamik programlama kullanarak en düşük toplam maliyeti hesaplar.

    Parametreler:
    - requests: Müşteri taleplerini temsil eden liste
    - agents: Müşteri temsilcilerinin konumlarını içeren liste

    Dönüş:
    - En düşük müşteri atama maliyeti
    """
    n = len(requests)  # Müşteri sayısı
    m = len(agents)  # Temsilci sayısı

    # DP tablosu oluşturuluyor
    dp = np.full((n + 1, m + 1), float('inf'))
    dp[0][0] = 0  # Başlangıç durumu

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Temsilci atanırsa maliyet hesaplanır
            cost = abs(requests[i - 1] - agents[j - 1])
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + cost)

    return dp[n][m]


# Zaman Karmaşıklığı: O(n*m)
# Uzay Karmaşıklığı: O(n*m)

# Pazarlama Kampanyası Seçimi - Knapsack Algoritması + DP

def maximize_marketing_roi(budget, campaigns):
    """
    Bütçeyi aşmadan maksimum yatırım getirisi (ROI) sağlayacak kampanyaları seçer.

    Parametreler:
    - budget: Kullanılabilir bütçe
    - campaigns: (maliyet, ROI) ikilileri içeren liste

    Dönüş:
    - Maksimum elde edilebilecek yatırım getirisi (ROI)
    """
    n = len(campaigns)
    dp = np.zeros((n + 1, budget + 1))

    for i in range(1, n + 1):
        cost, roi = campaigns[i - 1]
        for j in range(budget + 1):
            if j >= cost:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + roi)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][budget]


# Zaman Karmaşıklığı: O(n*budget)
# Uzay Karmaşıklığı: O(n*budget)

# Örnek Kullanım
requests = [1, 3, 5, 7]  # Müşteri talepleri
agents = [2, 4, 6, 8]  # Temsilciler
print("En düşük müşteri atama maliyeti:", optimize_agent_allocation(requests, agents))

campaigns = [(3, 60), (2, 100), (4, 120), (1, 40)]  # (maliyet, ROI)
budget = 5
print("En yüksek ROI:", maximize_marketing_roi(budget, campaigns))

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown("""
<div style="background:#101b32;padding:22px;border-radius:15px;color:#7dd3fc;text-align:center">
<h1>SAREVA</h1>
<p>Quantum AI Research Laboratory</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

shots = st.selectbox("Ölçüm Sayısı:", [100, 500, 1000, 5000], index=2)

if st.button("Simülasyonu Başlat"):
    rng = np.random.default_rng()
    angles = np.linspace(0, 2*np.pi, 100)
    signal = np.cos(angles)
    measured = signal + rng.normal(0, 1/np.sqrt(shots), size=len(angles))
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(angles, signal, label="Teorik sinyal")
    ax.scatter(angles, measured, s=12, label="Simülasyon ölçümleri")
    ax.set_title(f"SAREVA | Ölçüm sayısı: {shots}")
    ax.set_xlabel("Açı (radyan)")
    ax.set_ylabel("Sinyal")
    ax.legend()
    ax.grid(alpha=0.2)
    
    st.pyplot(fig)
    
    st.success("Simülasyon tamamlandı!")
    st.write(f"**Ölçüm sayısı:** {shots}")
    st.write(f"**Ortalama ölçülen sinyal:** {round(float(np.mean(measured)), 4)}")
    st.info("Not: Bu bir matematiksel simülasyondur.")

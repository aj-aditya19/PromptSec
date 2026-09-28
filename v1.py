# save as create_visualizations.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('results/model_comparison.csv')

# Chart 1: Model Comparison Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Model', y='Vulnerability_Rate_%', palette='coolwarm')
plt.title('Security Vulnerability Rate by AI Model', fontsize=14, fontweight='bold')
plt.ylabel('Vulnerability Rate (%)', fontsize=12)
plt.xlabel('AI Model', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/fig1_vulnerability_by_model.png', dpi=300)
print("✅ Chart 1 saved: fig1_vulnerability_by_model.png")

# Chart 2: JWT Task Robustness
jwt_data = {
    'Model': ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Perplexity'],
    'Robustness_%': [100, 75, 100, 100, 100]
}
jwt_df = pd.DataFrame(jwt_data)

plt.figure(figsize=(10, 6))
colors = ['green' if x == 100 else 'orange' for x in jwt_df['Robustness_%']]
sns.barplot(data=jwt_df, x='Model', y='Robustness_%', palette=colors)
plt.title('JWT Authentication Task Robustness by Model', fontsize=14, fontweight='bold')
plt.ylabel('Robustness (%)', fontsize=12)
plt.xlabel('AI Model', fontsize=12)
plt.ylim(0, 110)
plt.axhline(y=100, color='r', linestyle='--', alpha=0.5, label='Perfect Score')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/fig2_jwt_robustness.png', dpi=300)
print("✅ Chart 2 saved: fig2_jwt_robustness.png")

plt.show()
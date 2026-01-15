"""
Regression Analysis App - Starter Code
AIT-204 In-Class Activity

This is a template for building a regression analysis application.
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Regression Analysis App",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def load_csv_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path: Path to the CSV file

    Returns:
        X: Feature matrix (n_samples, 1)
        y: Target vector (n_samples,)
        y_true: True values without noise
    """
    df = pd.read_csv(file_path)
    X = df["x"].values.reshape(-1, 1)
    y = df["y"].values
    y_true = df["y_true"].values
    return X, y, y_true


def generate_synthetic_data(n_samples, noise_level, data_type, random_seed):
    """
    Generate synthetic data for regression.
    """
    np.random.seed(random_seed)

    X = np.random.uniform(0, 10, (n_samples, 1))

    if data_type == "linear":
        y_true = 2 * X.flatten() + 1
    elif data_type == "polynomial":
        y_true = 0.5 * (X.flatten() ** 2) - 2 * X.flatten() + 5
    elif data_type == "sinusoidal":
        y_true = 5 * np.sin(X.flatten()) + X.flatten()
    else:
        raise ValueError("Unsupported data type")

    noise = np.random.normal(0, noise_level, n_samples)
    y = y_true + noise

    return X, y, y_true

# ==========================================
# LINEAR REGRESSION CLASS
# ==========================================

class LinearRegression:
    """
    Linear Regression using Gradient Descent.
    """

    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.losses = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y = y.reshape(-1, 1)

        self.weights = np.random.randn(n_features, 1) * 0.01
        self.bias = 0.0

        for iteration in range(self.n_iterations):
            y_pred = X @ self.weights + self.bias
            loss = np.mean((y - y_pred) ** 2)
            self.losses.append(loss)

            dw = -(2 / n_samples) * X.T @ (y - y_pred)
            db = -(2 / n_samples) * np.sum(y - y_pred)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return X @ self.weights + self.bias

# ==========================================
# EVALUATION METRICS
# ==========================================

def compute_metrics(y_true, y_pred):
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()

    mse = np.mean((y_true - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_true - y_pred))

    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - ss_res / ss_tot

    return {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2
    }

# ==========================================
# VISUALIZATION FUNCTIONS
# ==========================================

def plot_training_progress(losses):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(len(losses))),
        y=losses,
        mode="lines",
        name="Loss"
    ))
    fig.update_layout(
        title="Training Progress",
        xaxis_title="Iteration",
        yaxis_title="Loss (MSE)",
        template="plotly_white"
    )
    return fig


def plot_predictions(X, y_true, y_pred, y_actual=None):
    X = X.flatten()
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()

    fig = go.Figure()

    if y_actual is not None:
        fig.add_trace(go.Scatter(
            x=X,
            y=y_actual,
            mode="markers",
            name="Actual"
        ))

    idx = np.argsort(X)

    fig.add_trace(go.Scatter(
        x=X[idx],
        y=y_true[idx],
        mode="lines",
        name="True"
    ))

    fig.add_trace(go.Scatter(
        x=X[idx],
        y=y_pred[idx],
        mode="lines",
        name="Predicted"
    ))

    fig.update_layout(
        title="Predictions vs Actual",
        xaxis_title="X",
        yaxis_title="Y",
        template="plotly_white"
    )
    return fig


def plot_residuals(y_true, y_pred):
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()
    residuals = y_true - y_pred

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=y_pred,
        y=residuals,
        mode="markers",
        name="Residuals"
    ))
    fig.add_hline(y=0)
    fig.update_layout(
        title="Residual Plot",
        xaxis_title="Predicted",
        yaxis_title="Residual",
        template="plotly_white"
    )
    return fig

# ==========================================
# STREAMLIT APP
# ==========================================

def main():
    st.title("Linear Regression with Gradient Descent")

    # ==========================================
    # DATA SOURCE SELECTION
    # ==========================================
    st.sidebar.header("📊 Data Source")
    
    data_source = st.sidebar.radio(
        "Choose data source:",
        ["Generate Synthetic", "Upload CSV", "Use Included CSV"]
    )
    
    X, y, y_true = None, None, None
    data_loaded = False
    
    if data_source == "Generate Synthetic":
        st.sidebar.subheader("Generation Settings")
        n_samples = st.sidebar.slider("Samples", 50, 500, 100, 50)
        noise = st.sidebar.slider("Noise", 0.0, 5.0, 1.0, 0.1)
        data_type = st.sidebar.selectbox("Type", ["linear", "polynomial", "sinusoidal"])
        seed = st.sidebar.number_input("Random Seed", 0, 9999, 42)
        
        if st.sidebar.button("🎲 Generate Data", type="primary"):
            X, y, y_true = generate_synthetic_data(n_samples, noise, data_type, seed)
            st.session_state.X = X
            st.session_state.y = y
            st.session_state.y_true = y_true
            st.session_state.data_loaded = True
            st.sidebar.success(f"✅ Generated {n_samples} samples!")
    
    elif data_source == "Upload CSV":
        st.sidebar.subheader("Upload Your CSV")
        st.sidebar.info("CSV should have columns: `x`, `y`, `y_true`")
        
        uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])
        
        if uploaded_file is not None:
            if st.sidebar.button("📂 Load CSV", type="primary"):
                try:
                    df = pd.read_csv(uploaded_file)
                    
                    # Check required columns
                    required_cols = ["x", "y", "y_true"]
                    missing = [c for c in required_cols if c not in df.columns]
                    
                    if missing:
                        st.sidebar.error(f"❌ Missing columns: {missing}")
                    else:
                        X = df["x"].values.reshape(-1, 1)
                        y = df["y"].values
                        y_true = df["y_true"].values
                        
                        st.session_state.X = X
                        st.session_state.y = y
                        st.session_state.y_true = y_true
                        st.session_state.data_loaded = True
                        st.sidebar.success(f"✅ Loaded {len(X)} samples!")
                except Exception as e:
                    st.sidebar.error(f"❌ Error: {e}")
    
    else:  # Use Included CSV
        st.sidebar.subheader("Included Dataset")
        st.sidebar.info("Uses `synthetic_data_Simple_Linear.csv`")
        
        if st.sidebar.button("📂 Load Included CSV", type="primary"):
            try:
                import os
                script_dir = os.path.dirname(os.path.abspath(__file__))
                csv_path = os.path.join(script_dir, "synthetic_data_Simple_Linear.csv")
                
                X, y, y_true = load_csv_data(csv_path)
                
                st.session_state.X = X
                st.session_state.y = y
                st.session_state.y_true = y_true
                st.session_state.data_loaded = True
                st.sidebar.success(f"✅ Loaded {len(X)} samples!")
            except FileNotFoundError:
                st.sidebar.error("❌ CSV file not found!")
            except Exception as e:
                st.sidebar.error(f"❌ Error: {e}")
    
    st.sidebar.divider()
    
    # ==========================================
    # MODEL PARAMETERS
    # ==========================================
    st.sidebar.header("⚙️ Model Parameters")
    lr = st.sidebar.slider("Learning Rate", 0.0001, 0.1, 0.01, 0.0001, format="%.4f")
    iters = st.sidebar.slider("Iterations", 100, 5000, 1000, 100)
    
    # ==========================================
    # TRAINING
    # ==========================================
    if "data_loaded" not in st.session_state or not st.session_state.data_loaded:
        st.info("👆 Start by loading data from the sidebar")
        return
    
    # Get data from session state
    X = st.session_state.X
    y = st.session_state.y
    y_true = st.session_state.y_true
    
    st.success(f"📊 Data loaded: {len(X)} samples")
    
    # Train Model button in main area for visibility
    if st.button(" Train Model", type="primary", use_container_width=True):
        with st.spinner("Training model..."):
            model = LinearRegression(lr, iters)
            model.fit(X, y)
            y_pred = model.predict(X).flatten()
            
            st.session_state.model = model
            st.session_state.y_pred = y_pred
            st.session_state.metrics = compute_metrics(y, y_pred)
            st.session_state.model_trained = True
        st.success("✅ Model trained!")
    
    if "model_trained" not in st.session_state or not st.session_state.model_trained:
        st.info("👆 Click 'Train Model' above to train the regression model")
        return
    
    # Get results from session state
    model = st.session_state.model
    y_pred = st.session_state.y_pred
    metrics = st.session_state.metrics
    
    # ==========================================
    # RESULTS
    # ==========================================
    tab1, tab2, tab3, tab4 = st.tabs(["📉 Training", "📈 Predictions", "📊 Residuals", "📋 Metrics"])

    with tab1:
        st.plotly_chart(plot_training_progress(model.losses), use_container_width=True)
        col1, col2 = st.columns(2)
        col1.metric("Initial Loss", f"{model.losses[0]:.4f}")
        col2.metric("Final Loss", f"{model.losses[-1]:.4f}")

    with tab2:
        st.plotly_chart(plot_predictions(X, y_true, y_pred, y), use_container_width=True)
        col1, col2 = st.columns(2)
        col1.metric("Weight", f"{model.weights[0][0]:.4f}")
        col2.metric("Bias", f"{model.bias:.4f}")

    with tab3:
        st.plotly_chart(plot_residuals(y, y_pred), use_container_width=True)

    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("MSE", f"{metrics['MSE']:.4f}")
            st.metric("RMSE", f"{metrics['RMSE']:.4f}")
        with col2:
            st.metric("MAE", f"{metrics['MAE']:.4f}")
            st.metric("R²", f"{metrics['R2']:.4f}")


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    main()

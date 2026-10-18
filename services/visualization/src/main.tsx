import React from "react";
import { createRoot } from "react-dom/client";

function App() {
  return (
    <main style={{ fontFamily: "system-ui", padding: "2rem", maxWidth: "760px", margin: "auto" }}>
      <h1>FIMAS Network Observatory</h1>
      <p>Visualization scaffold — connect this interface to validated simulation output.</p>
      <p>Research status: proposal and implementation in progress.</p>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);

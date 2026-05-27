import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_BASE_URL = "https://breathe-esg-backend-wndl.onrender.com";

function App() {
  const [activities, setActivities] = useState([]);
  const [file, setFile] = useState(null);
  const [sourceType, setSourceType] = useState("SAP");
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetchActivities();
  }, []);

  const fetchActivities = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/activities/`);
      setActivities(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const uploadCSV = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("source_type", sourceType);

    try {
      await axios.post(`${API_BASE_URL}/api/upload/`, formData);
      alert("CSV Uploaded Successfully");
      setFile(null);
      fetchActivities();
    } catch (error) {
      console.error(error);
      alert("CSV upload failed");
    }
  };

  const updateStatus = async (id, status) => {
    try {
      await axios.post(`${API_BASE_URL}/api/activities/${id}/status/`, {
        status: status,
      });

      fetchActivities();
    } catch (error) {
      console.error(error);
    }
  };

  const filteredActivities = activities.filter((item) =>
    item.activity_type.toLowerCase().includes(search.toLowerCase()) ||
    item.source_type.toLowerCase().includes(search.toLowerCase()) ||
    item.status.toLowerCase().includes(search.toLowerCase()) ||
    item.scope.toLowerCase().includes(search.toLowerCase())
  );

  const total = activities.length;
  const pending = activities.filter((item) => item.status === "pending").length;
  const suspicious = activities.filter((item) => item.status === "suspicious").length;
  const approved = activities.filter((item) => item.status === "approved").length;

  return (
    <div className="page">
      <h1>Breathe ESG Analyst Review Dashboard</h1>

      <p className="subtitle">
        Review normalized emissions activity data before auditor sign-off.
      </p>

      <div className="upload-box">
        <h2>Upload ESG Source Data</h2>

        <div className="upload-controls">
          <select
            value={sourceType}
            onChange={(e) => setSourceType(e.target.value)}
          >
            <option value="SAP">SAP Fuel / Procurement</option>
            <option value="UTILITY">Utility Electricity</option>
            <option value="TRAVEL">Corporate Travel</option>
          </select>

          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <button onClick={uploadCSV} className="upload-btn">
            Upload CSV
          </button>
        </div>
      </div>

      <div className="search-box">
        <input
          type="text"
          placeholder="Search by source, activity, scope or status..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      <div className="cards">
        <div className="card">
          <h3>Total Activities</h3>
          <p>{total}</p>
        </div>

        <div className="card">
          <h3>Pending Review</h3>
          <p>{pending}</p>
        </div>

        <div className="card warning">
          <h3>Suspicious Rows</h3>
          <p>{suspicious}</p>
        </div>

        <div className="card success">
          <h3>Approved</h3>
          <p>{approved}</p>
        </div>
      </div>

      <div className="table-box">
        <h2>Normalized Activity Records</h2>

        <table>
          <thead>
            <tr>
              <th>Source</th>
              <th>Scope</th>
              <th>Activity</th>
              <th>Quantity</th>
              <th>Unit</th>
              <th>Status</th>
              <th>Suspicious Reason</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {filteredActivities.map((item) => (
              <tr
                key={item.id}
                className={item.status === "suspicious" ? "suspicious-row" : ""}
              >
                <td>{item.source_type}</td>
                <td>{item.scope}</td>
                <td>{item.activity_type}</td>
                <td>{item.quantity}</td>
                <td>{item.normalized_unit}</td>
                <td>
                  <span className={`badge ${item.status}`}>
                    {item.status}
                  </span>
                </td>
                <td>{item.suspicious_reason || "-"}</td>
                <td>
                  <button
                    onClick={() => updateStatus(item.id, "approved")}
                    className="approve-btn"
                  >
                    Approve
                  </button>

                  <button
                    onClick={() => updateStatus(item.id, "rejected")}
                    className="reject-btn"
                  >
                    Reject
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
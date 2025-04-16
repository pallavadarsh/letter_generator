import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-gray-800 text-white px-4 py-3 shadow-md flex justify-between items-center">
      <h1 className="text-xl font-semibold">Accident Report AI System</h1>
      <div className="space-x-4">
        <Link to="/" className="hover:text-blue-300">
          Upload
        </Link>
        <Link to="/dashboard" className="hover:text-blue-300">
          Dashboard
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
import React from "react";

type SummaryCardProps = {
  summary: string;
};

const SummaryCard: React.FC<SummaryCardProps> = ({ summary }) => {
  return (
    <div className="bg-white rounded-lg shadow p-4 mt-4">
      <h2 className="text-lg font-semibold mb-2">Summary</h2>
      <p className="whitespace-pre-wrap text-gray-700">{summary}</p>
    </div>
  );
};

export default SummaryCard;
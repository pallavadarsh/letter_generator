import React from "react";

interface LetterViewerProps {
  letters: string[];
  currentIndex: number;
  handleNext: () => void;
  handlePrev: () => void;
}

const LetterViewer: React.FC<LetterViewerProps> = ({
  letters,
  currentIndex,
  handleNext,
  handlePrev
}) => {
  return (
    <div className="mt-6">
      <h3 className="text-lg font-semibold mb-2">
        Letter {currentIndex + 1} of {letters.length}
      </h3>
      <div className="bg-white p-4 rounded shadow mb-4">
        <pre className="whitespace-pre-wrap text-sm text-gray-800">
          {letters[currentIndex]}
        </pre>
      </div>
      <div className="flex justify-between">
        <button
          onClick={handlePrev}
          disabled={currentIndex === 0}
          className={`px-4 py-2 rounded shadow ${
            currentIndex === 0
              ? "bg-gray-300 text-gray-500"
              : "bg-blue-600 text-white hover:bg-blue-700"
          }`}
        >
          Previous
        </button>
        <button
          onClick={handleNext}
          disabled={currentIndex === letters.length - 1}
          className={`px-4 py-2 rounded shadow ${
            currentIndex === letters.length - 1
              ? "bg-gray-300 text-gray-500"
              : "bg-blue-600 text-white hover:bg-blue-700"
          }`}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default LetterViewer;

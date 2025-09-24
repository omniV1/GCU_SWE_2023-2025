import { Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart } from 'recharts';
import { Card } from "@/components/ui/card";

interface PerformanceChartProps {
  title: string;
  description: string;
  data: any[];
  lines: {
    key: string;
    name: string;
    color: string;
  }[];
}

/**
 * Renders a performance chart within a styled card component.
 *
 * @param {Object} props - The properties object.
 * @param {string} props.title - The title of the chart.
 * @param {string} props.description - The description of the chart.
 * @param {Array<Object>} props.data - The data to be displayed in the chart.
 * @param {Array<Object>} props.lines - The lines to be plotted on the chart.
 * @param {string} props.lines[].key - The key for the line data.
 * @param {string} props.lines[].name - The name of the line.
 * @param {string} props.lines[].color - The color of the line.
 * @returns {JSX.Element} The rendered performance chart component.
 */
export function PerformanceChart({ title, description, data, lines }: PerformanceChartProps) {
  return (
    <Card className="bg-[#1e1e1e] p-4 col-span-1">
      <h3 className="text-white text-lg font-semibold mb-4">{title}</h3>
      <p className="text-sm text-gray-400 mb-4">{description}</p>
      <div className="h-[300px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#333" />
            <XAxis dataKey="id" stroke="#666" />
            <YAxis stroke="#666" />
            <Tooltip 
              contentStyle={{ backgroundColor: '#1e1e1e', border: 'none' }}
              labelStyle={{ color: '#666' }}
            />
            <Legend />
            {lines.map((line) => (
              <Line
                key={line.key}
                type="monotone"
                dataKey={line.key}
                name={line.name}
                stroke={line.color}
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
}
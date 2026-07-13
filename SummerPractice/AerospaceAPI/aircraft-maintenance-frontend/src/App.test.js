import { render, screen } from '@testing-library/react';
import App from './App';
import { getAircrafts } from './services/api';

jest.mock('./services/api', () => ({
  getAircrafts: jest.fn(),
  deleteAircraft: jest.fn(),
}));

test('renders the aircraft list and primary navigation', async () => {
  getAircrafts.mockResolvedValue({
    data: [
      {
        id: 1,
        model: 'Cessna 172',
        serialNumber: 'TEST-172',
        lastMaintenanceDate: '2026-07-01T00:00:00Z',
      },
    ],
  });

  render(<App />);

  expect(await screen.findByText('TEST-172')).toBeInTheDocument();
  expect(screen.getByRole('heading', { name: /aircraft list/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /home/i })).toHaveAttribute('href', '/');
  expect(screen.getByRole('link', { name: /add aircraft/i })).toHaveAttribute(
    'href',
    '/add-aircraft'
  );
});

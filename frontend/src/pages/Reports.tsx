import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { 
  BarChart3Icon, 
  PieChartIcon, 
  TrendingUpIcon,
  DownloadIcon
} from 'lucide-react';
import { reportsAPI } from '../services';
import { LoadingSpinner } from '../components/common';
import { formatCurrency } from '../utils';

const Reports: React.FC = () => {
  const { data: inventorySummary, isLoading: inventoryLoading } = useQuery({
    queryKey: ['inventory-summary'],
    queryFn: reportsAPI.getInventorySummary,
  });

  const { data: salesSummary, isLoading: salesLoading } = useQuery({
    queryKey: ['sales-summary'],
    queryFn: reportsAPI.getSalesSummary,
  });

  const isLoading = inventoryLoading || salesLoading;

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Reports & Analytics</h1>
          <p className="text-gray-600">Business insights and analytics</p>
        </div>
        <button className="btn btn-primary flex items-center">
          <DownloadIcon className="h-5 w-5 mr-2" />
          Export Reports
        </button>
      </div>

      {isLoading ? (
        <div className="flex items-center justify-center h-64">
          <LoadingSpinner size="lg" />
        </div>
      ) : (
        <>
          {/* Report Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div className="card">
              <div className="flex items-center">
                <div className="bg-blue-500 rounded-md p-3">
                  <BarChart3Icon className="h-6 w-6 text-white" />
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500">
                    Inventory Categories
                  </p>
                  <p className="text-2xl font-bold text-gray-900">
                    {inventorySummary?.length || 0}
                  </p>
                </div>
              </div>
            </div>

            <div className="card">
              <div className="flex items-center">
                <div className="bg-green-500 rounded-md p-3">
                  <TrendingUpIcon className="h-6 w-6 text-white" />
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500">
                    Total Inventory Value
                  </p>
                  <p className="text-2xl font-bold text-gray-900">
                    {formatCurrency(
                      inventorySummary?.reduce((sum, item) => sum + item.total_value, 0) || 0
                    )}
                  </p>
                </div>
              </div>
            </div>

            <div className="card">
              <div className="flex items-center">
                <div className="bg-purple-500 rounded-md p-3">
                  <PieChartIcon className="h-6 w-6 text-white" />
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500">
                    Total Sales
                  </p>
                  <p className="text-2xl font-bold text-gray-900">
                    {formatCurrency(
                      salesSummary?.reduce((sum, item) => sum + item.total_amount, 0) || 0
                    )}
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Inventory Summary */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            <div className="card">
              <h3 className="text-lg font-medium text-gray-900 mb-4">
                Inventory by Category
              </h3>
              <div className="space-y-4">
                {inventorySummary?.map((item) => (
                  <div key={item.category} className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
                    <div>
                      <p className="font-medium text-gray-900">{item.category}</p>
                      <p className="text-sm text-gray-500">{item.count} items</p>
                    </div>
                    <div className="text-right">
                      <p className="font-medium text-gray-900">
                        {formatCurrency(item.total_value)}
                      </p>
                      <p className="text-sm text-gray-500">
                        {item.total_quantity.toFixed(2)} units
                      </p>
                    </div>
                  </div>
                ))}
                {(!inventorySummary || inventorySummary.length === 0) && (
                  <p className="text-gray-500 text-center py-4">No inventory data available</p>
                )}
              </div>
            </div>

            <div className="card">
              <h3 className="text-lg font-medium text-gray-900 mb-4">
                Sales by Status
              </h3>
              <div className="space-y-4">
                {salesSummary?.map((item) => (
                  <div key={item.status} className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
                    <div>
                      <p className="font-medium text-gray-900 capitalize">{item.status}</p>
                      <p className="text-sm text-gray-500">{item.count} orders</p>
                    </div>
                    <div className="text-right">
                      <p className="font-medium text-gray-900">
                        {formatCurrency(item.total_amount)}
                      </p>
                    </div>
                  </div>
                ))}
                {(!salesSummary || salesSummary.length === 0) && (
                  <p className="text-gray-500 text-center py-4">No sales data available</p>
                )}
              </div>
            </div>
          </div>

          {/* Quick Reports */}
          <div className="card">
            <h3 className="text-lg font-medium text-gray-900 mb-4">
              Quick Reports
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <button className="p-4 text-left border border-gray-200 rounded-md hover:bg-gray-50 transition-colors">
                <div className="font-medium text-gray-900">Inventory Report</div>
                <div className="text-sm text-gray-500">Current stock levels</div>
              </button>
              <button className="p-4 text-left border border-gray-200 rounded-md hover:bg-gray-50 transition-colors">
                <div className="font-medium text-gray-900">Sales Report</div>
                <div className="text-sm text-gray-500">Monthly sales summary</div>
              </button>
              <button className="p-4 text-left border border-gray-200 rounded-md hover:bg-gray-50 transition-colors">
                <div className="font-medium text-gray-900">Purchase Report</div>
                <div className="text-sm text-gray-500">Supplier analysis</div>
              </button>
              <button className="p-4 text-left border border-gray-200 rounded-md hover:bg-gray-50 transition-colors">
                <div className="font-medium text-gray-900">Financial Report</div>
                <div className="text-sm text-gray-500">Profit & loss statement</div>
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default Reports;
import axios from 'axios';
import type { 
  User, 
  LoginRequest, 
  Token, 
  InventoryItem, 
  InventoryItemCreate,
  SaleOrder,
  SaleOrderCreate,
  PurchaseOrder,
  PurchaseOrderCreate,
  Supplier,
  DashboardStats,
  InventorySummary,
  SalesSummary
} from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth API
export const authAPI = {
  login: async (credentials: LoginRequest): Promise<Token> => {
    const formData = new URLSearchParams();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);
    
    const response = await api.post('/auth/access-token', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    return response.data;
  },

  getCurrentUser: async (): Promise<User> => {
    const response = await api.post('/auth/test-token');
    return response.data;
  },
};

// Inventory API
export const inventoryAPI = {
  getItems: async (skip = 0, limit = 100): Promise<InventoryItem[]> => {
    const response = await api.get(`/inventory/?skip=${skip}&limit=${limit}`);
    return response.data;
  },

  getItem: async (id: number): Promise<InventoryItem> => {
    const response = await api.get(`/inventory/${id}`);
    return response.data;
  },

  createItem: async (item: InventoryItemCreate): Promise<InventoryItem> => {
    const response = await api.post('/inventory/', item);
    return response.data;
  },

  updateItem: async (id: number, item: Partial<InventoryItemCreate>): Promise<InventoryItem> => {
    const response = await api.put(`/inventory/${id}`, item);
    return response.data;
  },
};

// Sales API
export const salesAPI = {
  getOrders: async (skip = 0, limit = 100): Promise<SaleOrder[]> => {
    const response = await api.get(`/sales/?skip=${skip}&limit=${limit}`);
    return response.data;
  },

  getOrder: async (id: number): Promise<SaleOrder> => {
    const response = await api.get(`/sales/${id}`);
    return response.data;
  },

  createOrder: async (order: SaleOrderCreate): Promise<SaleOrder> => {
    const response = await api.post('/sales/', order);
    return response.data;
  },

  updateOrderStatus: async (id: number, status: string): Promise<void> => {
    await api.put(`/sales/${id}/status?status=${status}`);
  },
};

// Purchasing API
export const purchasingAPI = {
  getOrders: async (skip = 0, limit = 100): Promise<PurchaseOrder[]> => {
    const response = await api.get(`/purchasing/?skip=${skip}&limit=${limit}`);
    return response.data;
  },

  getOrder: async (id: number): Promise<PurchaseOrder> => {
    const response = await api.get(`/purchasing/${id}`);
    return response.data;
  },

  createOrder: async (order: PurchaseOrderCreate): Promise<PurchaseOrder> => {
    const response = await api.post('/purchasing/', order);
    return response.data;
  },

  getSuppliers: async (skip = 0, limit = 100): Promise<Supplier[]> => {
    const response = await api.get(`/purchasing/suppliers/?skip=${skip}&limit=${limit}`);
    return response.data;
  },

  createSupplier: async (supplier: Omit<Supplier, 'id' | 'created_at'>): Promise<Supplier> => {
    const response = await api.post('/purchasing/suppliers/', supplier);
    return response.data;
  },
};

// Reports API
export const reportsAPI = {
  getDashboardStats: async (): Promise<DashboardStats> => {
    const response = await api.get('/reports/dashboard');
    return response.data;
  },

  getInventorySummary: async (): Promise<InventorySummary[]> => {
    const response = await api.get('/reports/inventory/summary');
    return response.data;
  },

  getSalesSummary: async (): Promise<SalesSummary[]> => {
    const response = await api.get('/reports/sales/summary');
    return response.data;
  },
};

export default api;
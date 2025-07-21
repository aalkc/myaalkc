// API Types for Amanat Al-Kalima Company ERP

export interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  is_active: boolean;
  is_superuser: boolean;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface Token {
  access_token: string;
  token_type: string;
}

export interface InventoryItem {
  id: number;
  name: string;
  description?: string;
  category: string;
  sku: string;
  quantity: number;
  unit: string;
  unit_price: number;
  location?: string;
  minimum_stock?: number;
  created_at?: string;
  updated_at?: string;
}

export interface InventoryItemCreate {
  name: string;
  description?: string;
  category: string;
  sku: string;
  quantity: number;
  unit: string;
  unit_price: number;
  location?: string;
  minimum_stock?: number;
}

export interface Customer {
  id: number;
  name: string;
  email?: string;
  phone?: string;
  address?: string;
  city?: string;
  country?: string;
  tax_id?: string;
  created_at?: string;
}

export interface SaleOrder {
  id: number;
  order_number: string;
  customer_id: number;
  customer?: Customer;
  status: string;
  total_amount: number;
  currency: string;
  tax_amount?: number;
  discount_amount?: number;
  notes?: string;
  order_date?: string;
  delivery_date?: string;
  created_by?: number;
  created_at?: string;
  updated_at?: string;
}

export interface SaleOrderCreate {
  order_number: string;
  customer_id: number;
  total_amount: number;
  currency?: string;
  tax_amount?: number;
  discount_amount?: number;
  notes?: string;
  delivery_date?: string;
}

export interface Supplier {
  id: number;
  name: string;
  email?: string;
  phone?: string;
  address?: string;
  city?: string;
  country?: string;
  tax_id?: string;
  payment_terms?: string;
  created_at?: string;
}

export interface PurchaseOrder {
  id: number;
  order_number: string;
  supplier_id: number;
  supplier?: Supplier;
  status: string;
  total_amount: number;
  currency: string;
  tax_amount?: number;
  discount_amount?: number;
  notes?: string;
  order_date?: string;
  expected_delivery_date?: string;
  actual_delivery_date?: string;
  created_by?: number;
  created_at?: string;
  updated_at?: string;
}

export interface PurchaseOrderCreate {
  order_number: string;
  supplier_id: number;
  total_amount: number;
  currency?: string;
  tax_amount?: number;
  discount_amount?: number;
  notes?: string;
  expected_delivery_date?: string;
}

export interface DashboardStats {
  inventory: {
    total_items: number;
    total_value: number;
  };
  sales: {
    total_orders: number;
  };
  purchasing: {
    total_orders: number;
  };
}

export interface InventorySummary {
  category: string;
  count: number;
  total_quantity: number;
  total_value: number;
}

export interface SalesSummary {
  status: string;
  count: number;
  total_amount: number;
}
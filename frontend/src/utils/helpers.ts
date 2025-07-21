/**
 * Format currency amount for Saudi Riyal
 */
export const formatCurrency = (amount: number, currency = 'SAR'): string => {
  return new Intl.NumberFormat('ar-SA', {
    style: 'currency',
    currency: currency,
    minimumFractionDigits: 2,
  }).format(amount);
};

/**
 * Format date for Arabic locale
 */
export const formatDate = (date: string | Date): string => {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  return new Intl.DateTimeFormat('ar-SA', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }).format(dateObj);
};

/**
 * Format date and time for Arabic locale
 */
export const formatDateTime = (date: string | Date): string => {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  return new Intl.DateTimeFormat('ar-SA', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(dateObj);
};

/**
 * Generate order number
 */
export const generateOrderNumber = (prefix = 'ORD'): string => {
  const timestamp = Date.now().toString();
  const random = Math.random().toString(36).substring(2, 6).toUpperCase();
  return `${prefix}-${timestamp.slice(-8)}-${random}`;
};

/**
 * Calculate tax amount (Saudi VAT is 15%)
 */
export const calculateTax = (amount: number, taxRate = 0.15): number => {
  return amount * taxRate;
};

/**
 * Calculate total with tax
 */
export const calculateTotalWithTax = (amount: number, taxRate = 0.15): number => {
  return amount + calculateTax(amount, taxRate);
};

/**
 * Validate Saudi phone number
 */
export const isValidSaudiPhone = (phone: string): boolean => {
  const saudiPhoneRegex = /^(\+966|966|0)?5[0-9]{8}$/;
  return saudiPhoneRegex.test(phone.replace(/\s/g, ''));
};

/**
 * Format Saudi phone number
 */
export const formatSaudiPhone = (phone: string): string => {
  const cleaned = phone.replace(/\D/g, '');
  if (cleaned.startsWith('966')) {
    return `+${cleaned}`;
  } else if (cleaned.startsWith('5') && cleaned.length === 9) {
    return `+966${cleaned}`;
  } else if (cleaned.startsWith('05') && cleaned.length === 10) {
    return `+966${cleaned.substring(1)}`;
  }
  return phone;
};

/**
 * Get status color class for orders
 */
export const getStatusColor = (status: string): string => {
  switch (status.toLowerCase()) {
    case 'pending':
      return 'bg-yellow-100 text-yellow-800';
    case 'confirmed':
      return 'bg-blue-100 text-blue-800';
    case 'shipped':
    case 'received':
      return 'bg-purple-100 text-purple-800';
    case 'delivered':
      return 'bg-green-100 text-green-800';
    case 'cancelled':
      return 'bg-red-100 text-red-800';
    default:
      return 'bg-gray-100 text-gray-800';
  }
};

/**
 * Debounce function for search inputs
 */
export const debounce = <T extends (...args: any[]) => any>(
  func: T,
  wait: number
): ((...args: Parameters<T>) => void) => {
  let timeout: ReturnType<typeof setTimeout>;
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
};
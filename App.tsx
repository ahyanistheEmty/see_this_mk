
// see_this_mk/App.tsx

import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";
// import { ReactQueryDevtools } from "@tanstack/react-query-devtools"; // Conditionally enable for development only

import { AuthProvider } from "@generates/auth";
import { Root, Outlet, Routes } from "@generates/root";
import { SocketProvider } from "@generates/socket";

// Removed: import { RemixBrowser } from "@remix-run/react";
// Rationale: RemixBrowser is typically used in entry.client.tsx for hydration,
// and its presence here suggests it might be an unused import or placed incorrectly
// if this App.tsx is a root component for a client-side or different setup.
// If your project is a standard Remix app, this line is likely unnecessary in App.tsx.

import "./styles/index.css"; // Consider optimizing global style loading for large files

// Initialize QueryClient outside the component to prevent re-creation on re-renders
// Configure defaults for better cache management (e.g., staleTime, cacheTime)
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // Example: data is considered fresh for 5 minutes (300,000 ms)
      // After this, it will be refetched in the background when requested.
      staleTime: 1000 * 60 * 5,
      // Example: cached data is kept for 1 hour (3,600,000 ms) before garbage collection.
      // This allows quick re-render without refetch if data is still in cache, even if stale.
      cacheTime: 1000 * 60 * 60,
      // Consider setting to false if you want more control over when to refetch on window focus
      // refetchOnWindowFocus: true,
      // retry: 3, // Number of times to retry failed queries
    },
  },
});

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <SocketProvider>
          <Root>
            <Routes>
              <Outlet />
            </Routes>
          </Root>
        </SocketProvider>
      </AuthProvider>
      {/* 
        // Conditionally include ReactQueryDevtools for development only
        // Example: {process.env.NODE_ENV === "development" && <ReactQueryDevtools initialIsOpen={false} />}
      */}
    </QueryClientProvider>
  );
}

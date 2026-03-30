
#  TailwindCSS Crash Course: Essential Styles You Must Know

##  1. Colors & Backgrounds
Color utilities follow a simple pattern:  
`text-{color}-{shade}`, `bg-{color}-{shade}`, `border-{color}-{shade}`

### Common examples
- **Text colors**
    - `text-black`
    - `text-gray-600`
    - `text-blue-500`
- **Background colors**
    - `bg-white`
    - `bg-gray-100`
    - `bg-indigo-600`
- **Hover states**
    - `hover:bg-blue-700`
    - `hover:text-red-500`

---

#  2. Typography Essentials
Typography is one of Tailwind’s strongest areas.

### Font size
- `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl`, … `text-9xl`

### Font weight
- `font-light`
- `font-normal`
- `font-medium`
- `font-semibold`
- `font-bold`

### Text alignment
- `text-left`
- `text-center`
- `text-right`

### Line height & letter spacing
- `leading-tight`, `leading-relaxed`
- `tracking-tight`, `tracking-wide`

---

#  3. Spacing (Margin & Padding)
Spacing uses a scale: `0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32...`

### Margin
- `m-4` (all sides)
- `mx-4` (left & right)
- `my-2` (top & bottom)
- `mt-6`, `mb-3`, `ml-2`, `mr-1`

### Padding
- `p-4`
- `px-6`
- `py-3`

---

#  4. Layout: Flexbox & Grid

## Flexbox
- `flex`
- `flex-row` / `flex-col`
- `items-center` (align-items)
- `justify-between` (justify-content)
- `gap-4` (spacing between items)
- `flex-wrap`

### Example
```html
<div class="flex items-center justify-between p-4 bg-gray-100">
  <span>Logo</span>
  <button class="bg-blue-600 text-white px-4 py-2 rounded">Login</button>
</div>
```

## Grid
- `grid`
- `grid-cols-2`, `grid-cols-3`, `grid-cols-4`
- `gap-4`
- `col-span-2`

---

# 📦 5. Sizing (Width, Height)
### Width
- `w-full`
- `w-1/2`
- `w-64`
- `max-w-xl`

### Height
- `h-screen`
- `h-10`
- `min-h-full`

---

#  6. Borders & Radius
### Border
- `border`
- `border-2`
- `border-gray-300`

### Radius
- `rounded`
- `rounded-md`
- `rounded-lg`
- `rounded-full`

---

#  7. Shadows & Effects
- `shadow-sm`
- `shadow`
- `shadow-lg`
- `shadow-xl`
- `shadow-2xl`

---

#  8. Responsive Design (Super Important)
Tailwind uses **breakpoint prefixes**:

| Prefix | Screen |
|--------|---------|
| `sm:` | ≥ 640px |
| `md:` | ≥ 768px |
| `lg:` | ≥ 1024px |
| `xl:` | ≥ 1280px |
| `2xl:` | ≥ 1536px |

### Example
```html
<p class="text-base md:text-lg lg:text-xl">
  Responsive text size
</p>
```

---

#  9. Positioning
- `relative`
- `absolute`
- `fixed`
- `top-0`, `right-0`, `bottom-0`, `left-0`
- `z-10`, `z-50`

---

# 10. Transitions & Animations
### Transition
- `transition`
- `duration-300`
- `ease-in-out`

### Example
```html
<button class="bg-blue-600 hover:bg-blue-700 transition duration-300">
  Hover me
</button>
```

---

#  11. Display & Visibility
- `block`
- `inline-block`
- `hidden`
- `inline`
- `flex`
- `grid`

---

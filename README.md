## Build a Website about Scott Buying a House: Flask Design

### HTML Files
- `index.html`:
  - serves as the homepage for the website, featuring an introduction to Scott's house-buying journey and links to other pages.
- `house_search.html`:
  - provides a form for Scott to input his desired house preferences and search for available properties.
- `house_list.html`:
  - displays a list of properties that match Scott's preferences, incorporating images, prices, and other relevant details.
- `house_details.html`:
  - presents a detailed view of a specific property, including descriptions, amenities, a photo gallery, and contact information for scheduling viewings.
- `mortgage_calculator.html`:
  - incorporates a tool to help Scott calculate potential mortgage payments based on property price, interest rate, and loan term.
- `contact.html`:
  - offers a form for Scott to contact real estate agents or inquire about specific properties.

### Routes
- `/`:
  - Renders the `index.html` page as the homepage.
- `/house_search`:
  - Processes the preferences inputted in the `house_search.html` form, queries a database or external property listing API, and redirects to the `house_list.html` page with the results.
- `/house_list`:
  - Displays the list of properties matching Scott's preferences, allowing him to view details of each property by clicking on it.
- `/house_details/<property_id>`:
  - Renders the `house_details.html` page with the details of a specific property, where `property_id` is a unique identifier for the property.
- `/mortgage_calculator`:
  - Renders the `mortgage_calculator.html` page with a form to input property price, interest rate, and loan term, and calculates monthly mortgage payments.
- `/contact`:
  - Processes the information submitted in the `contact.html` form, capturing Scott's message and contact details, and sends it to the relevant party (e.g., real estate agent or property owner).
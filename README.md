# Physical AI & Humanoid Robotics Curriculum

This repository contains the curriculum and documentation for Physical AI & Humanoid Robotics.

## Project Structure

This project contains multiple directories:

- `my-docusaurus-site/` - The main Docusaurus documentation site
- `docs/` - Additional documentation files
- `history/` - Historical records and documentation
- `specs/` - Specification files for various features

## Building and Running the Documentation Site

The main documentation website is built using Docusaurus and is located in the `my-docusaurus-site` directory. To run or build the site:

### 1. Navigate to the Docusaurus site directory

```bash
cd my-docusaurus-site
```

### 2. Install dependencies

```bash
npm install
```

### 3. Run the development server

```bash
npm start
```

### 4. Build for production

```bash
npm run build
```

> **Note**: All Docusaurus commands must be run from within the `my-docusaurus-site` directory, as the configuration and assets are located there.

### Alternative: Run from project root

You can also run Docusaurus commands from the project root using:

```bash
cd my-docusaurus-site && npm run start
# or
cd my-docusaurus-site && npm run build
```

## Contributing

When making changes to the documentation, ensure you're editing files in the `my-docusaurus-site` directory, particularly:
- Documentation files in `my-docusaurus-site/docs/`
- Configuration in `my-docusaurus-site/docusaurus.config.ts`
- Custom CSS in `my-docusaurus-site/src/css/custom.css`
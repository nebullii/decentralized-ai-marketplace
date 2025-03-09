import path from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";
import MiniCssExtractPlugin from "mini-css-extract-plugin";
import CssMinimizerPlugin from "css-minimizer-webpack-plugin";
import TerserPlugin from "terser-webpack-plugin";
import { CleanWebpackPlugin } from "clean-webpack-plugin";
import webpack from "webpack";
import Dotenv from "dotenv-webpack";

const require = createRequire(import.meta.url);
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default {
    mode: "development", // Change to production when ready.
    entry: {
        main: [
            "./static/js/main.js",
            "./static/scss/styles.scss"
        ],
    },
    output: {
        path: path.resolve(__dirname, "static/dist"),
        filename: "[name].min.js",
    },
    resolve: {
        // Allow resolution of .mjs files.
        extensions: ['.mjs', '.js', '.json'],
        alias: {
            "process": "process/browser"
        },
        fallback: {
            process: require.resolve("process/browser")
        }
    },
    module: {
        rules: [
            {
                test: /memfs/,  // Ignore memfs
                use: 'null-loader'  // This prevents Webpack from bundling it
            },
            {
                test: /\.m?js$/,  // Handle both .mjs and .js files
                resolve: {
                    fullySpecified: false, // Allow imports without extensions
                },
            },
            // Ensure .mjs files in node_modules are handled as auto
            {
                test: /\.mjs$/,
                include: /node_modules/,
                type: "javascript/auto"
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ["@babel/preset-env"],
                    },
                },
            },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader",
                ],
            },
        ],
    },
    plugins: [
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({ filename: "styles.min.css" }),
        new Dotenv(),
        new webpack.ProvidePlugin({
            process: "process/browser"
        })
    ],
    optimization: {
        minimize: true,
        runtimeChunk: 'single',
        splitChunks: {
            chunks: "all",         // Splits vendor and runtime code.
            cacheGroups: {
                vendors: {
                    test: /[\\/]node_modules[\\/]/,
                    name: "vendors",
                    chunks: "all",
                },
            },
        },
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    format: {
                        comments: false,
                    },
                },
                extractComments: false,
            }),
            new CssMinimizerPlugin(),
        ],
    },
    watch: true,
};